# n8n Workflow Exports

Put only sanitized n8n workflow JSON exports in this folder.

## Recommended process

1. Open the workflow in n8n.
2. Export/download the workflow JSON.
3. Open the JSON in a text editor.
4. Search for:
   - `token`
   - `password`
   - `secret`
   - `api_key`
   - `apikey`
   - `authorization`
   - `credential`
   - `webhook`
   - your public domain
   - your private IP addresses
5. Remove or replace sensitive values.
6. Copy the sanitized JSON into this folder.
7. Run:

```bash
python3 ../../scripts/prepublish_check.py ../..
```

## Do not upload

Never upload the live n8n data directory:

```text
/home/node/.n8n
```

Do not upload:

```text
database.sqlite
credentials
encryption keys
OAuth tokens
production webhook secrets
```

## Recommended naming

```text
xiaozhi-message-router.json
telegram-ai-assistant.json
homelab-command-router.json
```

Only publish workflows you are comfortable making public.
