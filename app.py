import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/library")
def library():
    books = list(mongo.db.books.find())
    return render_template("library.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    genres = list(mongo.db.genres.find())
    if request.method == "POST":
        existing = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        if existing:
            flash(
                "Username is taken, try adding numbers or choose",
                "another username")
            return redirect(url_for("register"))

        if request.form.get("password") != request.form.get(
                "confirm-password"):
            flash("Your passwords did not match, please try again")
            return redirect(url_for("register"))

        register_user = {
            "first_name": request.form.get("first_name"),
            "surname": request.form.get("surname"),
            "email": request.form.get("email"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "genre": request.form.get("genre"),
        }
        mongo.db.users.insert_one(register_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        user_name = request.form.get("first_name")
        flash(
            f'Welcome {user_name}' +
            'you have been successfully registered.')
        return redirect(url_for("profile"))

    return render_template("register.html", genres=genres)


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
