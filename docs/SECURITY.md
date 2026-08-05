# Security Checklist

Before making the repository public, verify all of the following.

## Never commit

- `.env`
- OpenAI/API keys
- Telegram bot token
- passwords
- database credentials
- n8n credential database
- n8n encryption key
- SSH private keys
- TLS private keys
- Tailscale auth keys
- OAuth tokens
- production webhook secrets
- private certificates
- browser cookies/session tokens

## Review n8n exports

An exported workflow can reveal more than expected.

Inspect it for:

- hostnames
- domains
- webhook URLs
- internal IP addresses
- usernames
- email addresses
- node parameters
- static headers
- authorization strings
- credential references
- file system paths

## If a secret was ever committed

Deleting the line from the latest file is not enough because Git keeps history.

Immediately:

1. revoke/rotate the exposed secret;
2. remove it from Git history;
3. push the cleaned history;
4. verify it is no longer accessible.

Treat a committed secret as compromised.

## Public screenshots

Before uploading screenshots, check for:

- IP addresses
- domains
- QR codes
- API keys
- tokens
- email addresses
- usernames
- device serial numbers
- Wi-Fi SSIDs
- browser tabs containing private services

## Run local check

```bash
python3 scripts/prepublish_check.py .
```
