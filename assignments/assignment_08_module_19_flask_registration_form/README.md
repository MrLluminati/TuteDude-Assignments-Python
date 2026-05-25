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

## Step 3 - Read submitted form data using POST

### What I did

In Step 3, I changed the registration form so that it submits data using the POST method.

In `register.html`, I changed the form tag to:

```html
<form method="POST">
```

This means the form sends data to the Flask route when the Register button is clicked.

### Change made in app.py

I imported `request` from Flask:

```python
from flask import Flask, render_template, request
```

I also changed the home route so it can accept both GET and POST requests:

```python
@app.route("/", methods=["GET", "POST"])
```

Inside the route, I used `request.form.get()` to read the submitted form values:

```python
name = request.form.get("name")
email = request.form.get("email")
course = request.form.get("course")
```

For this step, I printed the submitted data in the terminal:

```python
print("Form submitted successfully.")
print("Name:", name)
print("Email:", email)
print("Course:", course)
```

### Test data used

I filled the form with:

```text
Full Name: Abhijeet Kumar
Email: abhikr14118@gmail.com
Course: Python
```

After clicking Register, the terminal displayed the submitted values.

### Output confirmed

The terminal showed:

```text
Form submitted successfully.
Name: Abhijeet Kumar
Email: abhikr14118@gmail.com
Course: Python
```

This confirms that Flask successfully received the submitted form data.

### What I learned

- A normal page load uses a GET request.
- A submitted form can use a POST request.
- `methods=["GET", "POST"]` allows the same Flask route to handle both page display and form submission.
- `request.form.get("name")` reads the value submitted from the input field whose name is `name`.
- The `name` attributes in the HTML form are important because Flask uses them to identify each submitted value.
- At this step, the data is only printed in the terminal. A success page will be added later.

### Screenshot proof

- [register.html POST method code](screenshot_proofs/step_03_post_form_data/step_03_a_register_html_post_method_code.png)
- [app.py request.form code](screenshot_proofs/step_03_post_form_data/step_03_b_app_py_request_form_code.png)
- [filled registration form in browser](screenshot_proofs/step_03_post_form_data/step_03_c_filled_form_browser.png)
- [terminal output showing submitted data](screenshot_proofs/step_03_post_form_data/step_03_d_terminal_printed_submitted_data.png)

---

## Progress checklist

- [x] Step 1: Basic Flask app and home page
- [x] Step 2: HTML registration form
- [x] Step 3: Read submitted form data using POST
- [ ] Step 4: Add simple validation
- [ ] Step 5: Add success page
- [ ] Step 6: Add basic CSS
- [ ] Step 7: Final testing and screenshots
- [ ] Step 8: Final packaging
