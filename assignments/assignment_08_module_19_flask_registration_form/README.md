# Assignment 8 - Flask Registration Form

## Project status

This assignment is being built fresh in a beginner-friendly way. The older files were removed so the project can be developed step by step with clear code, screenshots, and documentation.

## Project goal

The goal is to create a simple Flask web application with a student registration form.

Planned parts:

- basic Flask app
- HTML registration form
- POST form submission
- simple validation
- success page
- basic CSS
- screenshot proofs

## Current files

- `app.py` - main Flask application
- `requirements.txt` - required package list
- `templates/register.html` - HTML registration form
- `screenshot_proofs/` - proof screenshots

---

## Step 1 - Basic Flask app

### What I did

In Step 1, I created a simple Flask application in `app.py`.

The purpose of this step was to confirm that Flask is installed and that the local development server can run.

### Requirement added

`requirements.txt` contains:

```text
Flask
```

### Command used

```powershell
python .\app.py
```

### Browser URL

```text
http://127.0.0.1:5000
```

### Output confirmed

The browser showed the student registration heading and a short message saying that the Flask app is running.

### What I learned

- `Flask` is imported from the `flask` package.
- `app = Flask(__name__)` creates the Flask application.
- `@app.route("/")` creates the home route.
- The function below the route controls what is displayed in the browser.
- Running `app.py` starts the local Flask development server.

### Screenshot proof

- [basic app.py code and Flask server terminal](screenshot_proofs/step_01_basic_flask_app/step_01_a_basic_app_py_code_and_flask_server_terminal.png)
- [basic home page in browser](screenshot_proofs/step_01_basic_flask_app/step_01_b_basic_home_page_browser.png)

---

## Step 2 - HTML registration form

### What I did

In Step 2, I created a separate HTML file for the registration form.

I created this file:

```text
templates/register.html
```

The form currently displays three fields:

- Full Name
- Email
- Course

It also has a Register button.

At this step, the form only displays in the browser. The form submission logic will be added in the next step.

### Change made in app.py

In Step 1, the route directly returned HTML text from Python. In Step 2, I changed the route to load an HTML file using `render_template()`.

The import was changed to:

```python
from flask import Flask, render_template
```

The home route now returns:

```python
return render_template("register.html")
```

### Why templates are used

Templates keep HTML code separate from Python code. This makes the Flask project easier to read because:

- Python code stays in `app.py`;
- HTML page structure stays in `templates/register.html`;
- future CSS can be added separately in the `static` folder.

### Browser output confirmed

The browser displayed:

```text
Student Registration Form
Full Name
Email
Course
Register
```

This confirms that Flask successfully found and rendered the HTML template.

### What I learned

- Flask looks for HTML files inside the `templates` folder.
- `render_template()` is used to display an HTML file from Flask.
- `register.html` contains the visible form structure.
- The `name` attribute in an input field will later help Flask read submitted form data.
- At this stage, the form only displays; POST handling will be added later.

### Screenshot proof

- [register.html code and terminal](screenshot_proofs/step_02_html_registration_form/step_02_a_register_html_code_and_terminal.png)
- [app.py render_template code and terminal](screenshot_proofs/step_02_html_registration_form/step_02_b_app_py_render_template_code_and_terminal.png)
- [registration form in browser](screenshot_proofs/step_02_html_registration_form/step_02_c_registration_form_browser.png)

---

## Progress checklist

- [x] Step 1: Basic Flask app and home page
- [x] Step 2: HTML registration form
- [ ] Step 3: Read submitted form data using POST
- [ ] Step 4: Add simple validation
- [ ] Step 5: Add success page
- [ ] Step 6: Add basic CSS
- [ ] Step 7: Final testing and screenshots
- [ ] Step 8: Final packaging
