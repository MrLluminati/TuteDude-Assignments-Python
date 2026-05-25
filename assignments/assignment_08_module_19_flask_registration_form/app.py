# Assignment 8 - Flask Registration Form
# Step 2: Display an HTML registration form

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)