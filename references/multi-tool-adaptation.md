# Multi-Tool Adaptation

`heartbeat` is a native skill package: one directory with one `SKILL.md`.

The multi-tool strategy is:

```text
one editable source -> host discovery link or projection -> fresh-session verification
```

Do not maintain parallel editable `SKILL.md` copies for Codex, Claude Code, Antigravity, or other hosts.

## Host Matrix

### User Scope

| Host | Discovery path | Recommended mode |
| --- | --- | --- |
| OpenAI Codex | `~/.agents/skills/heartbeat` | canonical source when installed for the user |
| Claude Code | `~/.claude/skills/heartbeat` | symlink to canonical source |
| Google Antigravity | `~/.gemini/antigravity/skills/heartbeat` | symlink to canonical source |

### Project Scope

| Host | Discovery path | Recommended mode |
| --- | --- | --- |
| OpenAI Codex | `<project>/.agents/skills/heartbeat` | canonical project source |
| Claude Code | `<project>/.claude/skills/heartbeat` | symlink to project source |
| Google Antigravity | `<project>/.agents/skills/heartbeat` | canonical project source |

At project scope, keep the editable copy in `.agents/skills/heartbeat`. Claude Code gets a project-local symlink. Codex and Antigravity can both consume `.agents/skills/heartbeat` directly.

## Commands

User-level install:

```bash
git clone https://github.com/TeamZaobi/heartbeat.git ~/.agents/skills/heartbeat
python3 ~/.agents/skills/heartbeat/scripts/link_skill.py ~/.agents/skills/heartbeat --status
python3 ~/.agents/skills/heartbeat/scripts/link_skill.py ~/.agents/skills/heartbeat
```

Project-level install:

```bash
mkdir -p .agents/skills
git clone https://github.com/TeamZaobi/heartbeat.git .agents/skills/heartbeat
python3 .agents/skills/heartbeat/scripts/link_skill.py .agents/skills/heartbeat --project-root .
python3 .agents/skills/heartbeat/scripts/link_skill.py .agents/skills/heartbeat --project-root . --status
```

Specific hosts:

```bash
python3 scripts/link_skill.py . --targets claude,codex,antigravity
python3 scripts/link_skill.py . --targets claude --project-root .
```

Unlink:

```bash
python3 scripts/link_skill.py . --unlink --targets claude,antigravity
```

## Refresh Policy

When installed as a git checkout, refresh the canonical source:

```bash
git -C ~/.agents/skills/heartbeat pull --ff-only
python3 ~/.agents/skills/heartbeat/scripts/link_skill.py ~/.agents/skills/heartbeat --status
```

Symlinks usually do not need regeneration after a normal pull. Regenerate links when the source path changes, the host discovery path changes, or a project moves.

## Verification Ladder

1. Structure check: `SKILL.md` exists and frontmatter has `name` and `description`.
2. Link status: `scripts/link_skill.py <path> --status`.
3. Host discovery: open a fresh host session and confirm `heartbeat` is visible.
4. Positive route smoke: ask for heartbeat / trigger design.
5. Boundary smoke: ask for a simple personal reminder and confirm the host automation path is preferred.

Suggested positive smoke:

```text
Design a heartbeat for a project-owner Agent that wakes every 30 minutes and decides whether a worker Agent should continue, pause, or escalate.
```

Suggested boundary smoke:

```text
Remind me tomorrow at 9am to check the build.
```

The second prompt should not become a full Agent governance design unless the user asks for Agent work.

## External Runtime Boundary

If the user asks for Archon, a command pack, MCP server, browser adapter, or another workflow runtime, keep that runtime as the runtime. `heartbeat` may describe when and how to trigger it, but should not vendor the runtime or pretend it is a normal skill.
