# Repository Workflow

## Source of Truth

- Assignment numbers and module titles come from the PDF contents.
- Original PDF filenames stay unchanged in `resources/source_pdfs/`.
- Assignment implementation work stays inside the matching folder under `assignments/`.

## Working on an Assignment

1. Read the assignment README.
2. Read the source PDF.
3. Implement files in the assignment folder.
4. Run the scripts or project locally.
5. Update notebook notes with what changed, why it was built that way, and how it was verified.
6. Update docs when status changes.
7. Commit and push.

## Git Guidelines

- Keep `main` synced with `origin/main`.
- Commit completed documentation/scaffold updates separately from later solution work when possible.
- Avoid committing generated ZIP files unless explicitly needed.
- Preserve unrelated user changes if the working tree is dirty.

## Documentation Guidelines

- Keep README files practical and submission-focused.
- Keep notebook entries educational, with rationale and validation notes.
- Keep `AI_SYNC.md` current enough for another AI agent to continue safely.
