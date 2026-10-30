# `reflective-spec-plan` Examples

## Example 1

Input:

```text
Create a spec and task plan for migrating file uploads to signed URLs.
```

Expected output shape:

```markdown
## Definition of Ready check
## Spec
- Version: <spec version>; a mid-task change bumps it and marks spec_version-keyed artifacts stale
- Acceptance record: a named accepter closes it; execution success does not
## Usage
## Task Plan
## Definition of Done check
```

## Example 2

Input:

```text
Write tickets for adding audit logging to admin actions.
```

Expected output shape:

Tickets-only mode writes the TASK template, not titles alone. TASK-002 and TASK-003 use the same fields.

```markdown
### TASK-001: logging schema and event contract
- Goal:
- Spec Version:
- Scope:
- Inputs:
- Outputs:
- Dependencies:
- Authority / Data Boundary:
- Runtime / Tool Gates:
- Acceptance Criteria:
- Tests:
- Files likely touched:
- Risk:
- Parallelizable: yes/no
- Human Review Required: yes/no
### TASK-002: backend write path
### TASK-003: query and review UI
```

## Example 3 — Conditional Data / Result-Shape Decision

Input:

```text
Specify a document-parser API. A successful result carries a document with string text; a rejection carries a nonempty reason. Do not implement the parser.
```

Expected output excerpt (illustrative spec, not a parser implementation):

```markdown
## Data / result model
- Internal alternatives: Parsed(document: {text: string}) or Rejected(reason: nonempty string), not independent success/error flags.
- Each result has exactly one variant and its required payload. A sum-type implementation can exclude mixed or missing variant fields internally; this spec alone does not prove compiler enforcement.
- The example's wire format has exactly kind + document for parsed, or kind + reason for rejected; document has exactly one text string, which may be empty.
- Validate unknown external payloads against those shapes and the reason constraint before constructing an internal result. Arbitrary JSON can still contain forbidden combinations; rejecting it is a runtime boundary check. Revalidate at a later trust boundary when needed.

## Acceptance examples
| External payload | Expected boundary decision |
| --- | --- |
| {"kind":"parsed","document":{"text":"note"}} | Accept as Parsed |
| {"kind":"parsed","document":{"text":""}} | Accept as Parsed |
| {"kind":"rejected","reason":"unsupported format"} | Accept as Rejected |
| {"kind":"parsed","document":{"text":"note"},"reason":"bad"} | Reject mixed variant fields |
| {"kind":"parsed"} | Reject missing document |
| {"kind":"rejected","reason":""} | Reject empty reason |
| {"kind":"pending"} | Reject unknown variant |

## Failure signal / scope
- A mixed, missing-payload, empty-reason or unknown-variant payload is accepted, or a valid alternative is rejected.
- This model is relevant because the API changes result data. An unrelated copy-only edit needs no new domain model; no particular type system is mandated.
```
