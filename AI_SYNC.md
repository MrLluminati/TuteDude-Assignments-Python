# AI Sync: TuteDude Python Assignments

Last updated: 2026-05-11

## Purpose

This repository stores TuteDude Python assignment PDFs, implementation folders, submission planning docs, and learning notes. It is meant to stay useful for the owner and for future AI agents that continue the coursework.

## Current Repository State

- Remote: `https://github.com/MrLluminati/TuteDude-Assignments-Python.git`
- Default branch: `main`
- Visibility: private
- Assignment 1 has working scripts.
- All provided source PDFs are stored in `resources/source_pdfs/`.
- Remaining provided assignments are scaffolded with README files and notebook notes.

## Important Conventions

- Use PDF contents as the source of truth for assignment number and module.
- Preserve original PDF filenames exactly.
- Use folder names like `assignment_XX_module_YY_slug`.
- For duplicate printed assignment numbers, use the module number to disambiguate.
- Keep implementation, project files, and local test assets inside the matching assignment folder.
- Keep generated submission ZIP files out of Git unless the user explicitly asks to track them.
- Record learning notes in `notebook/`; summarize rationale and decisions, but do not attempt to expose private chain-of-thought.

## Read First

1. `README.md`
2. `docs/assignment_index.md`
3. `docs/source_pdf_map.md`
4. `docs/submission_plan.md`
5. The target assignment folder `README.md`
6. The target assignment notebook file

## Safe Next Actions

- Implement assignments one at a time, starting with Assignment 2 unless the user chooses another.
- After implementation, run the relevant script or project locally.
- Update the assignment README and notebook with validation notes.
- Commit and push changes to `main` when the user asks for GitHub sync.

## Known Gaps

- Assignment PDFs for 8 and 9 were not provided in the current source set.
- Later project assignments refer to course lecture practicals; implementation detail may require the course content or user-provided lecture requirements.
- Evidence-heavy assignments may need screenshots, screen recordings, or Drive links outside Git.
