# Python Bridge

This folder contains a small public reference bridge.

Your working deployment may contain additional Xiaozhi/MCP-specific behavior. Do not replace a working production bridge with this example unless you understand the differences.

## `mcp_pipe.py`

Reads one JSON object per line from standard input and POSTs it to `N8N_WEBHOOK_URL`.

Test:

```bash
export N8N_WEBHOOK_URL="http://127.0.0.1:5678/webhook-test/xiaozhi"
echo '{"message":"hello"}' | python3 mcp_pipe.py
```

## `mcp_stdio_client.py`

A generic stdio process launcher. It starts the command defined by `MCP_COMMAND` and forwards stdin/stdout.

It is provided mainly to demonstrate the process pattern used by a bridge service.

## Environment

Use `.env` outside Git or define variables through systemd.

Never hard-code:

- Telegram bot tokens
- API keys
- passwords
- Tailscale auth keys
- OAuth tokens
- webhook secrets
