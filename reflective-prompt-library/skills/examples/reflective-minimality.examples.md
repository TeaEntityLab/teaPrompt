# `reflective-minimality` Examples

## Example 1

Input:

```text
I need a PermissionManager class with a role hierarchy, caching layer, and audit-logging interface for the new feature.
```

Expected output shape:

```markdown
## Minimality Decision
- **skip**: PermissionManager class — existing auth middleware handles this
## Allowed Work
- one guard function in the route handler, ~5 lines
## Cut List
- PermissionManager class, role-hierarchy abstraction, caching layer,
  audit-logging interface
## Safety Floor
- existing auth checks must remain
## Verification
- existing auth tests pass
```

## Example 2

Input:

```text
We should add a validation library to handle the form data.
```

Expected output shape:

```markdown
## Minimality Decision
- **stdlib**: use built-in `Validator` / platform constraint, not a new dependency
## Cut List
- new library dependency
## Safety Floor
- validation coverage must match the existing test suite
## Verification
- one minimal check per field type
```
