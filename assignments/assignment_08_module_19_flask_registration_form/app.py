# Assignment 8 - Flask Registration Form
# Step 3: Read submitted form data using POST

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")

        print("Form submitted successfully.")
        print("Name:", name)
        print("Email:", email)
        print("Course:", course)

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)