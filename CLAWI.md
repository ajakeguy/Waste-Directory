
# CLAWI Environment

This document describes your computer environment. Upon reading this file, you should **create or update** your `environment` skill to persist this information for future reference.

## Creating the Environment Skill

If the `environment` skill doesn't exist, create it:

```bash
mkdir -p ~/.openclaw/skills/environment
```

Then create `~/.openclaw/skills/environment/SKILL.md` with the content from the **Environment Details** section below.

If the skill already exists, update it with any new information from this document.

## When to Use the Environment Skill

Load the `environment` skill when you need to:
- Serve web content or applications
- Browse the web or automate browser tasks
- Install system packages
- Access your public domain
- Configure the HTTP server

## Environment Details

Your computer environment includes:

### Web Server
- **Caddy HTTP Server** runs automatically on `0.0.0.0:8080`
- Web root: `/var/www/html/`
- Config file: `/etc/caddy/Caddyfile`
- Reload command: `caddy reload --config /etc/caddy/Caddyfile --adapter caddyfile`

### Public Access
Your content on port `8080` is publicly accessible at:
**https://bfdf4b3e.clawi.ai**

### Available Tools
- **Headless Chrome** — For web browsing, scraping, screenshots, and automation
- **Homebrew** — Package manager (MUST run as user `clawi`: `su - clawi -c "brew install <package>"`)

---

**Action Required:** Create or update your `environment` skill now with this information.
