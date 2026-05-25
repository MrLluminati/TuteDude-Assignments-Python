# Assignment 8 - Flask Registration Form
# Step 1: Basic Flask app

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Student Registration Form</h1><p>Flask app is running.</p>"


if __name__ == "__main__":
    app.run(debug=True)
