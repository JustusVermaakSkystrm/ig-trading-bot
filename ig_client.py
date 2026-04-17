"""
ig_client.py
------------
Handles all communication with the IG Markets REST API:
  - Authentication (login, token refresh)
  - GET / POST wrappers with automatic re-login on session expiry
  - Market search helper
  - Account info helper

Usage:
    from ig_client import IGClient
    client = IGClient.from_credentials_file("credentials.json")
    client.login()
"""

import json
import logging
import os
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


class IGClient:
    """Thin wrapper around the IG Markets REST API."""

    LIVE_URL = "https://api.ig.com/gateway/deal"
    DEMO_URL = "https://demo-api.ig.com/gateway/deal"

    def __init__(self, api_key: str, username: str, password: str,
                 account_id: str = None, demo: bool = False):
        self.api_key    = api_key
        self.username   = username
        self.password   = password
        self.account_id = account_id
        self.base_url   = self.DEMO_URL if demo else self.LIVE_URL

        # These are filled in after a successful login()
        self.cst            = None
        self.security_token = None

        self._session = requests.Session()

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------

    @classmethod
    def from_credentials_file(cls, path: str = "credentials.json") -> "IGClient":
        """
        Load credentials from a JSON file, falling back to environment variables.

        Environment variable names (used on servers where credentials.json
        is not present — never commit the file to git):
            IG_API_KEY, IG_USERNAME, IG_PASSWORD, IG_ACCOUNT_ID, IG_DEMO
        """
        if os.path.exists(path):
            with open(path) as f:
                creds = json.load(f)
        else:
            # Fall back to environment variables (server / CI deployment)
            logger.info("credentials.json not found — reading from environment variables.")
            creds = {
                "api_key":    os.environ["IG_API_KEY"],
                "username":   os.environ["IG_USERNAME"],
                "password":   os.environ["IG_PASSWORD"],
                "account_id": os.environ.get("IG_ACCOUNT_ID"),
                "demo":       os.environ.get("IG_DEMO", "false").lower() == "true",
            }
        return cls(
            api_key    = creds["api_key"],
            username   = creds["username"],
            password   = creds["password"],
            account_id = creds.get("account_id"),
            demo       = creds.get("demo", False),
        )

    # ------------------------------------------------------------------
    # Auth
    # ------------------------------------------------------------------

    def login(self) -> dict:
        """
        Authenticate with IG and store the CST + security tokens.
        Must be called before any other method.
        """
        url     = f"{self.base_url}/session"
        payload = {"identifier": self.username, "password": self.password,
                   "encryptedPassword": False}
        headers = self._build_headers(version="2")

        resp = self._session.post(url, json=payload, headers=headers)
        if not resp.ok:
            logger.error("IG login failed %s — body: %s", resp.status_code, resp.text)
        resp.raise_for_status()

        # Tokens live in response headers, not the body
        self.cst            = resp.headers["CST"]
        self.security_token = resp.headers["X-SECURITY-TOKEN"]

        data = resp.json()
        if not self.account_id:
            self.account_id = data.get("currentAccountId")

        # If the logged-in default account differs from our target, switch to it
        if self.account_id and data.get("currentAccountId") != self.account_id:
            logger.info("Switching to account %s...", self.account_id)
            self._switch_account(self.account_id)
        else:
            logger.info("Logged in to IG. Account ID: %s", self.account_id)

        return data

    def _switch_account(self, account_id: str):
        """Switch the active account (e.g. from CFD to spread bet)."""
        url  = f"{self.base_url}/session"
        resp = self._session.put(
            url,
            json={"accountId": account_id, "lightstreamerEndpoint": None},
            headers=self._build_headers(version="1"),
        )
        if resp.status_code == 200:
            logger.info("Switched to account %s", account_id)
        else:
            logger.warning("Account switch returned %s: %s", resp.status_code, resp.text[:200])

    def _refresh_if_needed(self, resp: requests.Response) -> bool:
        """Return True if we got a 401 and successfully re-logged in."""
        if resp.status_code == 401:
            logger.warning("Session expired — re-logging in.")
            self.login()
            return True
        return False

    # ------------------------------------------------------------------
    # Generic request helpers
    # ------------------------------------------------------------------

    def _build_headers(self, version: str = "1") -> dict:
        h = {
            "Content-Type":  "application/json",
            "Accept":        "application/json; charset=UTF-8",
            "X-IG-API-KEY":  self.api_key,
            "VERSION":       version,
        }
        if self.cst:
            h["CST"] = self.cst
        if self.security_token:
            h["X-SECURITY-TOKEN"] = self.security_token
        return h

    def get(self, endpoint: str, params: dict = None, version: str = "1") -> dict:
        """
        Authenticated GET request.
        Automatically re-logs in if the session has expired.
        """
        url  = f"{self.base_url}{endpoint}"
        resp = self._session.get(url, params=params, headers=self._build_headers(version))

        if self._refresh_if_needed(resp):
            resp = self._session.get(url, params=params, headers=self._build_headers(version))

        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint: str, payload: dict, version: str = "1") -> dict:
        """
        Authenticated POST request.
        Automatically re-logs in if the session has expired.
        """
        url  = f"{self.base_url}{endpoint}"
        resp = self._session.post(url, json=payload, headers=self._build_headers(version))

        if self._refresh_if_needed(resp):
            resp = self._session.post(url, json=payload, headers=self._build_headers(version))

        resp.raise_for_status()
        return resp.json()

    def delete(self, endpoint: str, payload: dict = None, version: str = "1") -> dict:
        """
        Authenticated DELETE request (used to close positions).
        IG uses a POST with a _method:DELETE override for some endpoints.
        """
        url     = f"{self.base_url}{endpoint}"
        headers = self._build_headers(version)
        headers["_method"] = "DELETE"
        resp = self._session.post(url, json=payload or {}, headers=headers)

        if self._refresh_if_needed(resp):
            resp = self._session.post(url, json=payload or {}, headers=headers)

        resp.raise_for_status()
        return resp.json()

    # ------------------------------------------------------------------
    # Convenience helpers
    # ------------------------------------------------------------------

    def search_markets(self, search_term: str) -> list:
        """
        Search for markets by name and return a list of results.
        Useful for finding the exact epic string for a market.

        Example:
            results = client.search_markets("EURUSD")
            for r in results["markets"]:
                print(r["epic"], r["instrumentName"])
        """
        return self.get("/markets", params={"searchTerm": search_term})

    def get_market_details(self, epic: str) -> dict:
        """Fetch full details (snapshot, dealing rules) for a given epic."""
        return self.get(f"/markets/{epic}", version="3")

    def get_accounts(self) -> dict:
        """List all accounts on this login (spread bet, CFD, etc.)."""
        return self.get("/accounts")

    def get_open_positions(self) -> dict:
        """Return all currently open positions."""
        return self.get("/positions", version="2")

    def get_working_orders(self) -> dict:
        """Return all working (pending) orders."""
        return self.get("/workingorders/otc")
