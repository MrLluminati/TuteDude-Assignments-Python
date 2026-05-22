from flask import Flask, render_template, request

app = Flask(__name__)

registered_users = []


def validate_registration_form(form_data):
    errors = {}

    name = form_data.get("name", "").strip()
    email = form_data.get("email", "").strip()
    phone = form_data.get("phone", "").strip()
    course = form_data.get("course", "").strip()
    password = form_data.get("password", "").strip()
    confirm_password = form_data.get("confirm_password", "").strip()

    if not name:
        errors["name"] = "Name is required."

    if not email:
        errors["email"] = "Email is required."
    elif "@" not in email or "." not in email:
        errors["email"] = "Enter a valid email address."

    if not phone:
        errors["phone"] = "Phone number is required."
    elif not phone.isdigit() or len(phone) != 10:
        errors["phone"] = "Phone number must contain exactly 10 digits."

    if not course:
        errors["course"] = "Please select a course."

    if not password:
        errors["password"] = "Password is required."
    elif len(password) < 6:
        errors["password"] = "Password must be at least 6 characters long."

    if password != confirm_password:
        errors["confirm_password"] = "Passwords do not match."

    cleaned_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "course": course,
    }

    return errors, cleaned_data


@app.route("/", methods=["GET"])
def home():
    return render_template("register.html", form_data={}, errors={})


@app.route("/register", methods=["POST"])
def register():
    errors, cleaned_data = validate_registration_form(request.form)

    if errors:
        return render_template(
            "register.html",
            form_data=request.form,
            errors=errors,
        ), 400

    registered_users.append(cleaned_data)
    return render_template("success.html", user=cleaned_data)


if __name__ == "__main__":
    app.run(debug=True)
