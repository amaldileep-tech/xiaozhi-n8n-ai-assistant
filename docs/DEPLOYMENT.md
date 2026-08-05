# Deployment Guide

This guide uses `/opt/xiaozhi-n8n-ai-assistant` as the portable installation path.

If your existing deployment lives elsewhere, update the paths in the service file instead of moving a working system unnecessarily.

## 1. Install requirements

Debian/Ubuntu example:

```bash
sudo apt update
sudo apt install -y git python3 python3-venv docker.io docker-compose-plugin
```

Check:

```bash
git --version
python3 --version
docker --version
docker compose version
```

## 2. Clone

```bash
cd /opt
sudo git clone https://github.com/YOUR_USERNAME/xiaozhi-n8n-ai-assistant.git
sudo chown -R "$USER":"$USER" /opt/xiaozhi-n8n-ai-assistant
cd /opt/xiaozhi-n8n-ai-assistant
```

## 3. Configure n8n

```bash
cp .env.example .env
nano .env
```

Start:

```bash
docker compose up -d
docker compose ps
```

Logs:

```bash
docker logs n8n --tail 100
```

## 4. Build bridge virtual environment

```bash
cd /opt/xiaozhi-n8n-ai-assistant/bridge
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 5. Create a private systemd environment file

```bash
sudo nano /etc/xiaozhi-mcp-bridge.env
```

Example:

```text
N8N_WEBHOOK_URL=http://127.0.0.1:5678/webhook/xiaozhi
BRIDGE_SHARED_SECRET=replace-with-a-long-random-secret
MCP_COMMAND=python3 -u mcp_pipe.py
```

Protect it:

```bash
sudo chmod 600 /etc/xiaozhi-mcp-bridge.env
```

## 6. Install systemd service

```bash
sudo cp /opt/xiaozhi-n8n-ai-assistant/systemd/xiaozhi-mcp-bridge.service \
  /etc/systemd/system/xiaozhi-mcp-bridge.service

sudo systemctl daemon-reload
sudo systemctl enable xiaozhi-mcp-bridge
sudo systemctl restart xiaozhi-mcp-bridge
```

Check:

```bash
sudo systemctl status xiaozhi-mcp-bridge --no-pager -l
```

Logs:

```bash
journalctl -u xiaozhi-mcp-bridge -f
```

## 7. Your existing `/mnt/docker` deployment

If your bridge already runs from a path such as:

```text
/mnt/docker/xiaozhi-mcp-bridge/
```

you can keep that structure.

Change only these lines in the service file:

```ini
WorkingDirectory=/mnt/docker/xiaozhi-mcp-bridge
ExecStart=/mnt/docker/xiaozhi-mcp-bridge/venv/bin/python /mnt/docker/xiaozhi-mcp-bridge/mcp_stdio_client.py
```

Do not publish your live environment file.

## 8. Updating code later

```bash
cd /opt/xiaozhi-n8n-ai-assistant
git pull
sudo systemctl restart xiaozhi-mcp-bridge
docker compose pull
docker compose up -d
```
