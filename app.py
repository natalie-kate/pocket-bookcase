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
                "another username"
                )
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
            "admin": "false"
        }
        mongo.db.users.insert_one(register_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        name = request.form.get("first_name")
        flash(
            f'Welcome {name} ' +
            'you have been successfully registered.')
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html", genres=genres)


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        existing = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        if existing:
            if check_password_hash(
              existing["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Your information did not",
                      "match our records, please try again.")
                return redirect(url_for("signin"))
        else:
            flash("Your information did not",
                  "match our records, please try again.")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    name = mongo.db.users.find_one(
        {"username": username})["first_name"]
    admin = mongo.db.users.find_one(
        {"username": username})["admin"]
    if session["user"]:
        return render_template("profile.html", name=name, admin=admin)


@app.route("/signout")
def signout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("signin"))


@app.route("/contact")
def contact():
    if session:
        name = mongo.db.users.find_one(
          {"username": session["user"]})["first_name"]
        surname = mongo.db.users.find_one(
          {"username": session["user"]})["surname"]
        email = mongo.db.users.find_one(
          {"username": session["user"]})["email"]
        return render_template(
            "contact.html", name=name, surname=surname, email=email)

    return render_template("contact.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    genres = list(mongo.db.genres.find())
    if request.method == "POST":
        is_series = "Yes" if request.form.get("series") else "No"
        existing_book = mongo.db.books.find_one(
            {"title": request.form.get("title").lower()}
        )
        if existing_book:
            flash("This book is already in our Library")
            return redirect(url_for("addbook"))
        else:
            title = request.form.get("title")
            book = {
                "title": title.lower(),
                "author": request.form.get("author").lower(),
                "synopsis": request.form.get("synopsis"),
                "series": is_series,
                "series_name": request.form.get("series_name").lower(),
                "genre": request.form.get("genre"),
                "cover_image": request.form.get("cover_image"),
                "rating": int(request.form.get("rating")),
                "review": request.form.get("review"),
                "added_by": session["user"]
                }
            mongo.db.books.insert_one(book)
            flash(
                "Thankyou for contributing to the library," +
                f'{title} has now been added'
                )
            return render_template("add-book.html", genres=genres)
    return render_template("add-book.html", genres=genres)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
