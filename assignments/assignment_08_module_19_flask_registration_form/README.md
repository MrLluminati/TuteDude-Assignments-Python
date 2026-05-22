# Portal Assignment 8: Module 19 - Flask Registration Form Project

Printed inside source document as:

```text
Assignment 11: Module 19 - Flask Registration Form Project
```

Source PDF:

```text
../../resources/source_pdfs/PORTAL_ASSIGNMENT_08_PRINTED_ASSIGNMENT_11_MODULE_19_FLASK_REGISTRATION_FORM.pdf
```

## Status

Implemented, locally tested, and ready for submission packaging.

## Project Scope

Build a Flask web application containing a student registration form with server-side validation, HTML templates, CSS styling, success page, and unit tests.

## Files

| File / Folder | Purpose |
| --- | --- |
| `app.py` | Main Flask application with routes and form validation. |
| `requirements.txt` | Python dependency list. |
| `templates/base.html` | Shared HTML layout. |
| `templates/register.html` | Registration form page. |
| `templates/success.html` | Successful registration page. |
| `static/style.css` | CSS styling for the form and success page. |
| `test_app.py` | Unit tests for page loading, invalid submission, and valid submission. |
| `screenshot_proofs/` | Proof screenshots for testing and browser output. |

## Features

- Student registration form.
- Server-side validation.
- Validation error display.
- Success page after valid registration.
- Basic CSS styling.
- Flask test client unit tests.

## Setup

```powershell
pip install -r requirements.txt
```

## Test

```powershell
python -m unittest .\test_app.py
```

## Run

```powershell
python .\app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

## Evidence Captured

Screenshot proofs include:

1. Terminal proof showing dependency installation, unit tests passing, Flask server running, and browser request logs.
2. Registration form page.
3. Invalid form submission with validation errors.
4. Successful registration page.

## Submission Checklist

- [x] Implement Flask app.
- [x] Add templates.
- [x] Add CSS styling.
- [x] Add server-side validation.
- [x] Add unit tests.
- [x] Test form rendering.
- [x] Test valid and invalid submissions.
- [x] Capture screenshot proofs.
- [ ] Create ZIP from this folder.
- [ ] Upload to Drive and verify sharing access if required.