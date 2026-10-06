# headless-agent-cli-contract — Examples

## Example 1 — read-only proposal via stdin transport (ollama)

Input:

```text
Emit the invocation recipe for ollama (qwen2.5-coder:1.5b), mode read-only-proposal, prompt from task prompt file.
```

Expected output shape:

```markdown
## Inventory probe
- command -v ollama → /usr/local/bin/ollama; `ollama list` shows qwen2.5-coder:1.5b cached (zero credit, daemon must be running)

## Recipe (ollama / read-only-proposal)
- transport: stdin — `ollama run qwen2.5-coder:1.5b < prompt.txt` (or argv string; stdin preferred)
- permission flags: none needed for read-only (no tool surface in run mode)
- output isolation: stdout carries proposal + spinner glyphs + timing tail; capture stdout/stderr separately
- strip list: spinner block + `total duration:`/`eval count:` stats — channel varies (observed on stdout 2026-10-06 run A, on stderr with stats absent in run B); strip BOTH streams before scoring
- malformed spellings: none observed; `ollama run` without a model name is a usage error, not a recipe
- BLOCKED: n/a
```

## Example 2 — argv transport with trust flag (cursor-agent / devin)

```markdown
## Recipe (devin swe-2-max / read-only-proposal)
- transport: argv — `devin --respect-workspace-trust false --model swe-2-max -p "<prompt>"` (array-form exec; `-p -` treats the literal dash as the prompt — never use it)
- permission flags: headless auto-denies tool calls; prompt must inline file contents (no read tools) or the call returns a tool-rejection warning only
- output isolation: stdout = proposal; stderr may carry warnings
- strip list: none observed
- BLOCKED: n/a

## Recipe (cursor-agent / read-only-proposal)
- transport: argv — `cursor-agent -f -p --output-format text "<prompt>"` (-f/--trust required headlessly)
- permission flags: -f trusts the directory only; keep default tool permissions (no --yolo)
- side-channels: stderr `claude-mem …` hook lines may precede the proposal — strip; they are side-path noise, not model output
```

## Example 3 — provider policy denial = BLOCKED, not failure (agy)

```text
agy --model <provider-model> --effort low --print="<prompt>"
```

Observed: headless mode auto-denied a `command` tool permission and produced no proposal. Correct verdict:

```markdown
- BLOCKED: agy headless requires a `command(<target>)` allow-rule in settings.json
  for tool-using mode; read-only proposal prompts must not trigger tool calls —
  do NOT add --dangerously-skip-permissions to unblock (human-approved widenings only).
```
