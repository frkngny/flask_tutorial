from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> This is home page </h1>"


@app.route("/sign_in", methods=["POST", "GET"])
def sign_in():
    if request.method == "POST":
        user_name = request.form["name"]
        return redirect(url_for("user", you=user_name))
    else:
        return render_template("3_index.html")


@app.route("/<you>")
def user(you):
    return f"<p>Hello {you}!</p>"


if __name__ == "__main__":
    app.run(debug=True)



