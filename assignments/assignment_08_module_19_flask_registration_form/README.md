# Assignment 8 - Flask Registration Form

This project is being built fresh in a beginner-friendly way with step-wise code, screenshots, and notes.

## Project goal

Create a simple Flask web application with a student registration form.

## Current files

- `app.py` - main Flask application
- `requirements.txt` - required package list
- `templates/register.html` - registration form page
- `templates/success.html` - success page after valid submission
- `static/style.css` - basic CSS styling
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

## Step 5 - Success page after valid registration

I created a new template file:

```text
templates/success.html
```

This page is shown only after the form is submitted with valid data.

In `app.py`, after successful validation, I return the success page and pass the submitted values to it:

```python
return render_template(
    "success.html",
    name=name,
    email=email,
    course=course
)
```

The success page displays:

- registration successful message;
- submitted full name;
- submitted email;
- submitted course;
- a link to register another student.

What I learned:

- A Flask route can return different templates depending on the situation.
- If validation fails, the app returns `register.html` with an error message.
- If validation passes, the app returns `success.html` with submitted details.
- Variables passed from `app.py` can be shown in HTML using Jinja syntax like `{{ name }}`.
- A normal link such as `<a href="/">` can take the user back to the form page.

Screenshot proof:

- [blank registration form before success test](screenshot_proofs/step_05_success_page/step_05_a_blank_registration_form_before_success_test.png)
- [filled form before submit](screenshot_proofs/step_05_success_page/step_05_b_filled_form_before_submit.png)
- [success page in browser](screenshot_proofs/step_05_success_page/step_05_c_success_page_browser.png)
- [register another student link back to form](screenshot_proofs/step_05_success_page/step_05_d_register_another_student_link_back_to_form.png)
- [app.py success page code and terminal](screenshot_proofs/step_05_success_page/step_05_e_app_py_success_page_code_and_terminal.png)
- [success.html code and terminal](screenshot_proofs/step_05_success_page/step_05_f_success_html_code_and_terminal.png)

---

## Step 6 - Basic CSS and HTML cleanup

I created a CSS file:

```text
static/style.css
```

Then I linked it in both HTML templates using:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

I also cleaned the HTML structure in `register.html` and `success.html`.

The cleanup included:

- adding `lang="en"` to the `<html>` tag;
- adding `<meta charset="UTF-8">`;
- adding the viewport meta tag;
- connecting labels and inputs with `for` and `id`;
- removing inline CSS from the error message;
- using the `.error` CSS class instead;
- adding a `.container` class for page layout.

What I learned:

- Flask serves static files from the `static` folder.
- `url_for('static', filename='style.css')` correctly links CSS in Flask templates.
- CSS keeps styling separate from HTML.
- Proper labels improve HTML quality and accessibility.
- Meta tags help the browser understand encoding and screen scaling.
- VS Code Problems panel can help identify HTML warnings before submission.

Screenshot proof:

- [style.css code top](screenshot_proofs/step_06_basic_css_and_html_cleanup/step_06_a1_style_css_code_top.png)
- [style.css code bottom](screenshot_proofs/step_06_basic_css_and_html_cleanup/step_06_a2_style_css_code_bottom.png)
- [register.html cleaned code and no problems](screenshot_proofs/step_06_basic_css_and_html_cleanup/step_06_b_register_html_cleaned_code_and_no_problems.png)
- [success.html cleaned code](screenshot_proofs/step_06_basic_css_and_html_cleanup/step_06_c_success_html_cleaned_code.png)
- [styled registration form in browser](screenshot_proofs/step_06_basic_css_and_html_cleanup/step_06_d_styled_registration_form_browser.png)
- [styled validation error in browser](screenshot_proofs/step_06_basic_css_and_html_cleanup/step_06_e_styled_validation_error_browser.png)
- [styled filled form in browser](screenshot_proofs/step_06_basic_css_and_html_cleanup/step_06_f_styled_filled_form_browser.png)
- [styled success page in browser](screenshot_proofs/step_06_basic_css_and_html_cleanup/step_06_g_styled_success_page_browser.png)
- [register another student link back to form](screenshot_proofs/step_06_basic_css_and_html_cleanup/step_06_h_register_another_student_back_to_form.png)

---

## Progress checklist

- [x] Step 1: Basic Flask app and home page
- [x] Step 2: HTML registration form
- [x] Step 3: Read submitted form data using POST
- [x] Step 4: Add simple validation
- [x] Step 5: Add success page
- [x] Step 6: Add basic CSS
- [ ] Step 7: Final testing and screenshots
- [ ] Step 8: Final packaging
