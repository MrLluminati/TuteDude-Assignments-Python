# Assignment 8 - Flask Registration Form

This project is being built fresh in a beginner-friendly way with step-wise code, screenshots, and notes.

## Project goal

Create a simple Flask web application with a student registration form.

## Current files

- `app.py` - main Flask application
- `requirements.txt` - required package list
- `templates/register.html` - registration form page
- `screenshot_proofs/` - screenshots for each step

---

## Step 1 - Basic Flask app

I created a simple Flask application and confirmed that the local server runs at:

```text
http://127.0.0.1:5000
```

What I learned:

- `Flask` is imported from the `flask` package.
- `app = Flask(__name__)` creates the Flask app.
- `@app.route("/")` creates the home page route.
- `app.run(debug=True)` starts the local development server.

Screenshot proof:

- [basic app.py code and Flask server terminal](screenshot_proofs/step_01_basic_flask_app/step_01_a_basic_app_py_code_and_flask_server_terminal.png)
- [basic home page in browser](screenshot_proofs/step_01_basic_flask_app/step_01_b_basic_home_page_browser.png)

---

## Step 2 - HTML registration form

I created `templates/register.html` and changed `app.py` to use `render_template("register.html")`.

The page displays a basic registration form with fields for name, contact, and course information.

What I learned:

- Flask searches for HTML files inside the `templates` folder.
- `render_template()` keeps HTML separate from Python code.
- Input `name` attributes are needed so Flask can read submitted form values later.

Screenshot proof:

- [register.html code and terminal](screenshot_proofs/step_02_html_registration_form/step_02_a_register_html_code_and_terminal.png)
- [app.py render_template code and terminal](screenshot_proofs/step_02_html_registration_form/step_02_b_app_py_render_template_code_and_terminal.png)
- [registration form in browser](screenshot_proofs/step_02_html_registration_form/step_02_c_registration_form_browser.png)

---

## Step 3 - Read submitted form data using POST

I changed the form to use `method="POST"` and updated the Flask route to support both `GET` and `POST` requests.

The app now reads submitted values using `request.form.get()` and prints them in the terminal.

What I learned:

- `GET` is used for opening the page normally.
- `POST` is used when the form is submitted.
- `methods=["GET", "POST"]` allows one route to handle both.
- `request.form.get()` reads submitted form values.

Screenshot proof:

- [register.html POST method code](screenshot_proofs/step_03_post_form_data/step_03_a_register_html_post_method_code.png)
- [app.py request.form code](screenshot_proofs/step_03_post_form_data/step_03_b_app_py_request_form_code.png)
- [filled registration form in browser](screenshot_proofs/step_03_post_form_data/step_03_c_filled_form_browser.png)
- [terminal output showing submitted data](screenshot_proofs/step_03_post_form_data/step_03_d_terminal_printed_submitted_data.png)

---

## Step 4 - Simple form validation

I added basic validation so that blank form submissions are not accepted.

In `app.py`, I used an `error` variable. If any field is blank, the app sets:

```python
error = "All fields are required."
```

In `register.html`, I used a Jinja `if` condition to show the error message only when it exists.

What I learned:

- Form validation means checking user input before accepting it.
- A blank string means a field was left empty.
- `or` can check whether any one required field is blank.
- Flask can pass variables from Python into an HTML template.
- Jinja can conditionally display an error message on the page.

Screenshot proof:

- [app.py validation code](screenshot_proofs/step_04_simple_validation/step_04_a_app_py_validation_code.png)
- [register.html error display code and terminal](screenshot_proofs/step_04_simple_validation/step_04_b_register_html_error_display_code_and_terminal.png)
- [blank form validation error in browser](screenshot_proofs/step_04_simple_validation/step_04_c_blank_form_validation_error_browser.png)
- [valid form filled in browser](screenshot_proofs/step_04_simple_validation/step_04_d_valid_form_filled_browser.png)

---

## Progress checklist

- [x] Step 1: Basic Flask app and home page
- [x] Step 2: HTML registration form
- [x] Step 3: Read submitted form data using POST
- [x] Step 4: Add simple validation
- [ ] Step 5: Add success page
- [ ] Step 6: Add basic CSS
- [ ] Step 7: Final testing and screenshots
- [ ] Step 8: Final packaging
