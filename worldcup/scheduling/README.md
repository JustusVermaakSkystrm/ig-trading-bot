# Hourly trigger via macOS launchd

GitHub's own cron throttles scheduled workflows to roughly every 2-3 hours
with occasional gaps. This launchd agent reliably triggers the
`worldcup-hourly.yml` workflow every hour while your Mac is awake (and once
on wake if it slept through a fire time). The workflow itself still does all
the work in the cloud — this only kicks it off.

## One-time setup (~5 minutes)

### 1. Create a GitHub token

Create a **fine-grained personal access token**:
https://github.com/settings/tokens?type=beta

- Repository access: **Only select repositories** → `ig-trading-bot`
- Permissions → **Actions: Read and write**
- Expiration: your choice (you'll re-create it when it lapses)

Copy the token (starts with `github_pat_`).

### 2. Store the token in the Keychain (not on disk)

```bash
security add-generic-password -a "$USER" -s worldcup-gh-token -w 'github_pat_PASTE_HERE'
```

### 3. Install the script and agent

```bash
# from your local clone of the repo:
mkdir -p ~/Library/Scripts
cp worldcup/scheduling/worldcup-trigger.sh ~/Library/Scripts/
chmod +x ~/Library/Scripts/worldcup-trigger.sh

# fill the placeholders in the plist and install it
sed -e "s#REPLACE_WITH_SCRIPT_PATH#$HOME/Library/Scripts/worldcup-trigger.sh#" \
    -e "s#REPLACE_WITH_HOME#$HOME#g" \
    worldcup/scheduling/com.worldcup.predictor.hourly.plist \
    > ~/Library/LaunchAgents/com.worldcup.predictor.hourly.plist

launchctl load ~/Library/LaunchAgents/com.worldcup.predictor.hourly.plist
```

`RunAtLoad` makes it fire immediately, so you can verify right away.

## Verify

```bash
tail ~/Library/Logs/worldcup-trigger.log        # should show "OK: workflow dispatched"
```

Then check the run appear under the repo's Actions tab, or watch the site's
"Last checked" timestamp advance within a couple of minutes.

## Manage

```bash
# stop
launchctl unload ~/Library/LaunchAgents/com.worldcup.predictor.hourly.plist
# rotate the token later
security delete-generic-password -s worldcup-gh-token
security add-generic-password -a "$USER" -s worldcup-gh-token -w 'github_pat_NEW'
```

## Notes

- While the Mac is asleep the hour is skipped, then self-heals on wake. For
  true 24/7 coverage independent of your Mac, an external cron service is the
  only option, at the cost of storing the token off-device.
- The token only grants Actions read/write on this one repo — worst case if
  leaked is someone running your prediction workflow.
