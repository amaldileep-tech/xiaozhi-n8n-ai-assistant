# Xiaozhi + n8n AI Assistant

A self-hosted AI automation project connecting a Xiaozhi ESP32-S3 voice device to an n8n automation server through a lightweight Python bridge.

The goal of this repository is to document a practical home-lab AI assistant architecture while keeping credentials, tokens, private URLs, and server data out of Git.

## Architecture

```text
Xiaozhi ESP32-S3
       |
       | voice / MCP messages
       v
Python MCP Bridge
(mcp_pipe.py / mcp_stdio_client.py)
       |
       | HTTP / webhook / automation request
       v
      n8n
       |
       +-------------------+
       |                   |
       v                   v
   AI services         Telegram
       |
       v
Home-lab automations / APIs
```

## What this project demonstrates

- Linux service administration
- Python integration
- systemd service management
- Docker / Docker Compose
- n8n workflow automation
- REST/webhook integrations
- ESP32 / Xiaozhi integration
- AI-agent orchestration
- home-lab deployment and troubleshooting
- secure handling of secrets

## Repository layout

```text
xiaozhi-n8n-ai-assistant/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── LICENSE
├── README.md
├── bridge/
│   ├── mcp_pipe.py
│   ├── mcp_stdio_client.py
│   ├── requirements.txt
│   └── README.md
├── systemd/
│   └── xiaozhi-mcp-bridge.service
├── n8n/
│   └── workflows/
│       └── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   ├── GITHUB_UPLOAD.md
│   └── SECURITY.md
├── scripts/
│   └── prepublish_check.py
├── screenshots/
│   └── .gitkeep
└── .github/
    └── workflows/
        └── prepublish-check.yml
```

## Quick start

### 1. Clone

```bash
git clone https://github.com/YOUR_USERNAME/xiaozhi-n8n-ai-assistant.git
cd xiaozhi-n8n-ai-assistant
```

### 2. Create your local environment file

```bash
cp .env.example .env
nano .env
```

Never commit `.env`.

### 3. Start n8n

```bash
docker compose up -d
docker compose ps
```

By default this example binds n8n only to:

```text
127.0.0.1:5678
```

That is intentional. Expose it externally only through a secure reverse proxy, VPN, or another access method you control.

### 4. Test the sample Python bridge

The included bridge is a safe demonstration implementation. It reads JSON lines from standard input and forwards them to the configured n8n webhook.

```bash
cd bridge
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Example:

```bash
echo '{"message":"hello from Xiaozhi"}' | python mcp_pipe.py
```

### 5. Install the systemd unit

Read `docs/DEPLOYMENT.md` first.

```bash
sudo cp systemd/xiaozhi-mcp-bridge.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable xiaozhi-mcp-bridge
sudo systemctl start xiaozhi-mcp-bridge
sudo systemctl status xiaozhi-mcp-bridge --no-pager -l
```

## Your real n8n workflows

Do not blindly upload your live n8n database or Docker volume.

Export only the workflows you want to publish and inspect the exported JSON first.

Place sanitized exports here:

```text
n8n/workflows/
```

See `n8n/workflows/README.md`.

## Before publishing

Run:

```bash
python3 scripts/prepublish_check.py .
```

Then inspect:

```bash
git status
git diff --cached
```

Only push after the secret check returns clean.

## Suggested GitHub description

> Self-hosted AI assistant integrating Xiaozhi ESP32-S3, Python MCP bridge, n8n, Telegram and home-lab automations using Docker and Linux.

## Suggested GitHub topics

```text
xiaozhi
esp32
esp32-s3
n8n
mcp
docker
linux
python
automation
ai-agent
homelab
systemd
telegram-bot
devops
```

## Important

The bridge code included in this public template is a reference implementation. If your current production bridge contains additional logic, copy that code only after removing credentials and reviewing any upstream license requirements.

## License

MIT. See `LICENSE`.
