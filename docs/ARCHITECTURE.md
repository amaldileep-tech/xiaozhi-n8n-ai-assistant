# Architecture

## Components

### 1. Xiaozhi ESP32-S3

Acts as the voice/device interface.

Typical responsibilities:

- microphone / speaker interaction
- sending requests to the AI/backend layer
- receiving assistant responses
- interacting with MCP-enabled services

### 2. Python MCP bridge

Runs as a Linux service.

The bridge separates the device-side integration from the automation platform.

A public architecture can be represented as:

```text
Xiaozhi
   |
   v
MCP / stdio / message layer
   |
   v
Python bridge
   |
   v
n8n webhook/API
```

### 3. n8n

n8n handles orchestration such as:

- Telegram messaging
- AI model calls
- API requests
- notifications
- home-lab actions
- conditional logic
- workflow history

### 4. Docker

n8n is deployed as a container so the service is easier to reproduce, update and maintain.

### 5. systemd

The Python bridge is kept alive using a systemd unit.

Benefits:

- starts at boot
- automatic restart
- standard Linux logging
- status monitoring

Useful commands:

```bash
sudo systemctl status xiaozhi-mcp-bridge --no-pager -l
sudo systemctl restart xiaozhi-mcp-bridge
journalctl -u xiaozhi-mcp-bridge -f
```

## Data flow

```text
User voice
   |
   v
Xiaozhi ESP32-S3
   |
   v
MCP bridge
   |
   v
n8n
   |
   +--> AI model
   |
   +--> Telegram
   |
   +--> API / home-lab service
   |
   v
Response/action
```

## Security boundary

Public Git repository:

```text
source code
documentation
example environment file
sanitized workflow exports
architecture diagrams
```

Private server:

```text
real .env
API keys
Telegram token
n8n credentials
database
private URLs
SSH keys
Tailscale credentials
production webhook secrets
```
