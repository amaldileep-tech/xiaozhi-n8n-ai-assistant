# Xiaozhi + n8n AI Assistant

A self-hosted AI automation project integrating a **Xiaozhi ESP32-S3 voice assistant**, **n8n**, **Linux**, **Docker**, **MCP**, and external services inside a home-lab environment.

This repository documents the architecture, deployment method, automation workflow, security approach, and troubleshooting involved in building the system.

## Project Overview

```text
User Voice
    |
    v
Xiaozhi ESP32-S3
    |
    v
Xiaozhi MCP Proxy
    |
    v
Linux / MCP Bridge
    |
    v
n8n Automation
    |
    +-----------------------+
    |           |           |
    v           v           v
AI Services   Telegram   Home-Lab APIs
    |
    v
Response / Automation Action
```

## Technologies Used

- Linux
- Raspberry Pi / Home Lab
- Docker / Docker Compose
- n8n
- Python
- MCP
- systemd
- ESP32-S3 / Xiaozhi
- Telegram integration
- REST APIs / Webhooks
- Git / GitHub / GitHub Actions

## What I Implemented

- Deployed and maintained the integration on a Linux home-lab server
- Ran n8n using Docker
- Integrated Xiaozhi with n8n through an MCP bridge
- Created n8n automation workflows
- Managed the MCP bridge using systemd
- Configured automatic startup and restart
- Kept credentials outside source code using environment variables
- Integrated external APIs and messaging services
- Troubleshot connectivity, TLS, Docker, n8n, and Linux service issues
- Built a Git-based documentation and deployment workflow
- Added automated repository safety checks with GitHub Actions

## n8n Workflow

A sanitized version of the real workflow is available at:

```text
n8n/workflows/xiaozhi-mcp-workflow.json
```

Sensitive information was removed before publication.

## Xiaozhi MCP Bridge

The communication bridge is based on the open-source **xiaozhi-mcp-proxy** project:

https://github.com/maojindao55/xiaozhi-mcp-proxy

Version used:

```text
081900cc1cc5e2b026c49dbb7f85bff9e238fdc9
```

The upstream bridge source code is not presented as my own work. This repository focuses on deployment, integration, automation, Linux service management, and the surrounding infrastructure.

See:

```text
bridge/README.md
```

## Linux Service Management

The MCP bridge runs as:

```text
xiaozhi-mcp-bridge.service
```

Example service file:

```text
systemd/xiaozhi-mcp-bridge.service
```

Useful commands:

```bash
sudo systemctl status xiaozhi-mcp-bridge
sudo systemctl restart xiaozhi-mcp-bridge
journalctl -u xiaozhi-mcp-bridge -f
```

## Security

Secrets are intentionally kept outside Git. The repository does not include API keys, passwords, Telegram bot tokens, OAuth tokens, Tailscale auth keys, SSH private keys, n8n credential databases, production webhook secrets, or private environment files.

Example values are stored only in:

```text
.env.example
```

Before publishing changes:

```bash
python3 scripts/prepublish_check.py .
```

GitHub Actions also performs an automated safety check.

## Repository Structure

```text
xiaozhi-n8n-ai-assistant/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── docker-compose.yml
├── bridge/
│   └── README.md
├── n8n/
│   └── workflows/
│       ├── README.md
│       └── xiaozhi-mcp-workflow.json
├── systemd/
│   └── xiaozhi-mcp-bridge.service
├── docs/
├── scripts/
│   └── prepublish_check.py
└── .github/
    └── workflows/
        └── prepublish-check.yml
```

## Skills Demonstrated

- Linux administration
- Git and GitHub workflow
- Docker and Docker Compose
- n8n automation
- MCP integration
- AI and API orchestration
- Networking and remote access
- systemd service management
- Secret handling and repository sanitization
- CI safety checks

## Future Improvements

- Additional n8n workflows
- Better monitoring and health checks
- Infrastructure-as-Code experiments
- Local AI model integration
- Expanded MCP tools
- Centralized logging and monitoring

## Disclaimer

This is a personal home-lab and learning project. Third-party projects and services remain the property of their respective authors and maintainers.

## License

Repository-specific content is provided under the MIT License unless otherwise stated. Third-party components retain their original licenses.
