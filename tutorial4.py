from flask import Flask, render_template, request, redirect, url_for, session
import datetime

app = Flask(__name__)
app.secret_key = "mykey"
app.permanent_session_lifetime = datetime.timedelta(minutes=1)


@app.route("/")
def home():
    return "<h1> This is home page </h1>"


@app.route("/sign_in", methods=["POST", "GET"])
def sign_in():
    if request.method == "POST":
        session.permanent = True
        user_name = request.form["name"]
        session["user_name"] = user_name
        return redirect(url_for("user"))
    else:
        if "user_name" in session:
            return redirect(url_for("user"))
        return render_template("3_index.html")


@app.route("/user")
def user():
    if "user_name" in session:
        you = session["user_name"]
        return f"<p>Hello {you}!</p>"
    else:
        return redirect(url_for("sign_in"))


@app.route("/sign_out")
def sign_out():
    session.pop("user_name")
    return redirect(url_for("sign_in"))


if __name__ == "__main__":
    app.run(debug=True)


