from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! Welcome to flask tutorial! <h1>HELLO</h1>"


@app.route("/<name>")
def user(name):
    return f"Hello {name}"


@app.route("/profile")
def profile():
    return redirect(url_for("user", name="Coder!"))


if __name__ == "__main__":
    app.run()
