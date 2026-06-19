# True hourly via cron-job.org (external trigger)

GitHub's built-in scheduler throttles our `worldcup-hourly.yml` cron to roughly
every 3–6 hours. To force a genuine hourly run, have the free service
**cron-job.org** call the workflow's dispatch endpoint every hour. It runs in
the cloud (no Mac needed) and stacks on top of GitHub's own cron — extra runs
are harmless (a run with no new data still just refreshes the heartbeat).

## 1. Create a GitHub token (least-privilege)
https://github.com/settings/tokens?type=beta → **Generate new token**
- **Token name:** `worldcup-cron`
- **Expiration:** 90 days (longest convenient; you'll re-create it when it lapses)
- **Repository access:** *Only select repositories* → **`ig-trading-bot`**
- **Permissions → Repository permissions → Actions:** **Read and write**
- Generate, copy the `github_pat_…` value (shown once).

Blast radius if leaked: triggering/cancelling Actions on this one public repo. Nothing else.

## 2. Create the cron-job.org job
Sign up (free) at https://cron-job.org, then **Create cronjob**:

- **Title:** `World Cup hourly trigger`
- **URL:**
  ```
  https://api.github.com/repos/JustusVermaakSkystrm/ig-trading-bot/actions/workflows/worldcup-hourly.yml/dispatches
  ```
- **Schedule:** Every hour — "Every day", "Every hour", minute `5` (any minute; :05 avoids GitHub's own :47 slot).

Then open **Advanced / "Show advanced settings"**:
- **Request method:** `POST`
- **Custom HTTP headers** (add each as a Name / Value pair):
  | Name | Value |
  |------|-------|
  | `Accept` | `application/vnd.github+json` |
  | `Authorization` | `Bearer github_pat_PASTE_YOUR_TOKEN` |
  | `X-GitHub-Api-Version` | `2022-11-28` |
  | `Content-Type` | `application/json` |
- **Request body:**
  ```json
  {"ref":"main"}
  ```
- **Treat as success:** HTTP status `2xx` (GitHub returns **204 No Content** on success — that's a success).
- **Save** and make sure the job is **enabled**.

## 3. Test it
- In cron-job.org, use **"Test run" / "Execute now"** → expect **HTTP 204**.
- Then check the repo's **Actions** tab: a new run of "Hourly World Cup prediction
  update" with event **workflow_dispatch** should appear within seconds.
- Or watch the site's **"Last checked"** timestamp advance.

## Notes
- **Success = HTTP 204** (empty body). If cron-job.org shows 401/403, the token
  is missing the **Actions: Read and write** permission or the repo wasn't
  selected. 404 usually means the workflow filename/owner/repo in the URL is off.
- **Token expiry:** when it lapses, regenerate (step 1) and update the
  `Authorization` header value in the cron-job.org job.
- **Cadence:** cron-job.org free tier supports hourly easily (down to every
  minute). Hourly is plenty.
- This does **not** replace GitHub's native cron or the optional Mac `launchd`
  job — they all hit the same dispatch and any extra/duplicate run is a no-op
  beyond refreshing the timestamp.
