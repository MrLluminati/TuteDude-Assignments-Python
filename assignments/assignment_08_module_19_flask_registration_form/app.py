# Assignment 8 - Flask Registration Form
# Step 4: Add simple form validation

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    error = ""

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")

        if name == "" or email == "" or course == "":
            error = "All fields are required."
        else:
            print("Form submitted successfully.")
            print("Name:", name)
            print("Email:", email)
            print("Course:", course)

    return render_template("register.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)