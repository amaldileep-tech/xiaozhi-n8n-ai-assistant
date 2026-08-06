# Security

This repository is public and contains only sanitized configuration and workflow examples.

## Never Commit

- `.env` files
- API keys or tokens
- passwords
- Telegram bot tokens
- n8n credentials or encryption keys
- SSH/TLS private keys
- Tailscale authentication keys
- production webhook secrets

## n8n Workflow Exports

Before publishing an n8n workflow, review it for:

- credentials
- webhook IDs/secrets
- internal IP addresses
- private URLs
- tokens or authorization headers
- personal data

## Secret Exposure

If a secret is accidentally committed:

1. Revoke or rotate it immediately.
2. Remove it from Git history.
3. Push the cleaned history.
4. Verify the old secret no longer works.

## Before Publishing

Run:

```bash
python3 scripts/prepublish_check.py .
