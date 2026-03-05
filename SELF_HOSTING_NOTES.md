# Self-Hosting Evaluation - VPS on Used MacBook

**Status:** Deferred — adding to project backlog

## Chosen Approach
- **Hardware:** Used MacBook (already owned)
- **Infrastructure:** VPS (Virtual Private Server)
- **Rationale:** Familiar hardware, don't need to buy new (Pi), portable if needed

## Pros
- $0 hardware cost (reuse MacBook)
- Familiar environment (macOS)
- Can develop locally, deploy to VPS
- Easier debugging than headless Pi
- Battery backup built-in (laptop)

## Cons
- Higher power draw than Pi (but idle MacBook is ~10-20W)
- Need to keep it plugged in for "always on"
- More moving parts than a Pi setup

## Next Steps (when we cycle back)
1. Choose VPS provider (Hetzner, DigitalOcean, AWS Lightsail, Vultr)
2. Docker setup on VPS
3. OpenClaw Gateway deployment
4. Telegram bot migration
5. API key configuration (Brave/Perplexity)
6. Workspace backup strategy

## Migration Path from clawi.ai
- Export workspace files (MEMORY.md, USER.md, research/, etc.)
- Import to new self-hosted instance
- Conversation history likely lost (infrastructure-layer)
- Re-authenticate Telegram bot with new Gateway

---
*Added: March 3, 2026*
