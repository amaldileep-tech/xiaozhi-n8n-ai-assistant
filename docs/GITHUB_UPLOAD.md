# GitHub Upload Guide

## 1. Create an empty GitHub repository

Suggested repository name:

```text
xiaozhi-n8n-ai-assistant
```

Suggested description:

```text
Self-hosted AI assistant using Xiaozhi ESP32-S3, Python MCP bridge, n8n, Docker and Linux.
```

You can start it as `Private`, inspect everything, then change it to `Public`.

## 2. Copy this repository to your Linux machine

Example:

```bash
cd /mnt/docker
mkdir -p xiaozhi-n8n-ai-assistant
```

Copy the package contents into it.

## 3. Add your sanitized real files

If your working bridge currently contains files such as:

```text
mcp_pipe.py
mcp_stdio_client.py
```

compare them with the public examples.

Do not overwrite your working files blindly.

For GitHub, copy the sanitized versions into:

```text
bridge/
```

## 4. Add sanitized n8n workflow exports

Put them in:

```text
n8n/workflows/
```

Do not copy the n8n Docker volume.

## 5. Run the security check

From repository root:

```bash
python3 scripts/prepublish_check.py .
```

Fix anything it reports.

## 6. Initialize Git

```bash
git init
git branch -M main
git status
```

## 7. First commit

```bash
git add .
git status
git diff --cached
git commit -m "Initial public release of Xiaozhi n8n AI assistant"
```

Read the staged diff before pushing.

## 8. Connect GitHub

Replace the URL:

```bash
git remote add origin https://github.com/YOUR_USERNAME/xiaozhi-n8n-ai-assistant.git
```

Check:

```bash
git remote -v
```

## 9. Push

```bash
git push -u origin main
```

GitHub may ask you to authenticate using a browser, credential manager, SSH key, or personal access token depending on your Git configuration.

## 10. Future changes

```bash
git status
git add .
git commit -m "Describe the change"
git push
```

## Recommended first public version

Publish:

```text
README.md
docs/
bridge/ sanitized code
docker-compose.yml
.env.example
.gitignore
systemd/
sanitized n8n workflow exports
architecture screenshots/diagram
```

Keep private:

```text
.env
live database
tokens
keys
credentials
server backups
complete Docker volume
private logs
```
