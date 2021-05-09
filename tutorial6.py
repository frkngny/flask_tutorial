from flask import Flask, render_template, request, redirect, url_for, session, flash
import datetime
from DatabaseManager import DatabaseManager

app = Flask(__name__)
app.secret_key = "mykey"
app.permanent_session_lifetime = datetime.timedelta(minutes=1)
dbm = DatabaseManager(app)


@app.route("/")
def home():
    dbm.create_table()
    return render_template("5_index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user_email = request.form["email"]

        mysql_db = dbm.get_users()
        flag = 0
        for usr in mysql_db:
            if usr['email'] == user_email:
                flag += 1
                session["user_email"] = user_email
                session["user_name"] = usr['name']
                return redirect(url_for("user"))
        if flag == 0:
            flash("There is no such a mail!", "info")
            return redirect(url_for("login"))

    else:
        return render_template("login.html")


@app.route("/sign_up", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        session.permanent = True
        user_name = request.form["name"]
        user_email = request.form["email"]

        mysql_db = dbm.get_users()
        flag = 0
        for usr in mysql_db:
            if usr['email'] == user_email:
                flag += 1
                session["user_email"] = user_email
                session["user_name"] = user_name
                return redirect(url_for("login"))
        if flag == 0:
            dbm.add_user(user_name, user_email)
            flash("You have successfully signed up!", "info")
        return redirect(url_for("login"))
    else:
        return render_template("sign_up.html")


@app.route("/user")
def user():
    if "user_name" in session:
        you = session["user_name"]
        return render_template("profile.html", you=you)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user_name")
    session.pop("user_email")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)


