# WACOS Repository Guidance

These instructions apply to the entire WACOS repository.

## Git Push Authentication

- This Windows checkout uses ordinary Git with the configured `manager` credential helper (Windows Git Credential Manager) for fetch and push operations.
- An expired or unauthenticated GitHub CLI (`gh`) session does **not** by itself block `git fetch` or `git push`.
- When the user asks only to commit or push repository changes, use the established Git workflow: inspect scope, stage explicit files, commit, and run `git push`.
- Do not require `gh auth login` unless an operation specifically needs GitHub CLI or GitHub API authentication, such as creating or managing a pull request through `gh`.
- Before telling the user authentication is required, attempt the requested ordinary Git operation through the configured credential helper. Ask for reauthentication only after that Git operation returns an actual credential or authorization failure.
- If sandbox restrictions prevent Git from writing `.git` metadata or reaching the remote, request the narrowly scoped escalation needed for `git fetch`, `git add`, `git commit`, or `git push`; do not misdiagnose a sandbox denial as a GitHub authentication failure.

## Publishing Scope

- This repository has an established history of direct pushes to `main` when the user explicitly requests a push.
- Stage only the files belonging to the requested change. Do not stage generated output, temporary QA files, local exports, or unrelated untracked directories unless the user explicitly includes them.
