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
    if session["user"]:
        admin = mongo.db.users.find_one(
          {"username": session["user"]})["admin"]
        return render_template("library.html", books=books, admin=admin)

    return render_template("library.html", books=books)


@app.route("/search_library", methods=["GET", "POST"])
def search_library():
    if request.method == "POST":
        search = request.form.get("search").lower()
        results = list(mongo.db.books.find(
            {"$text": {"$search": search}}))
        if results:
            if session["user"]:
                admin = mongo.db.users.find_one(
                  {"username": session["user"]})["admin"]
                return render_template(
                    "library.html", admin=admin, results=results)
            return render_template(
              "library.html", results=results)
        else:
            flash(f"Sorry cannot find { search.title()}")
            return redirect(url_for("library"))


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


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
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
                return redirect(url_for("sign_in"))
        else:
            flash("Your information did not",
                  "match our records, please try again.")
            return redirect(url_for("sign_in"))

    return render_template("sign-in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    name = mongo.db.users.find_one(
        {"username": username})["first_name"]
    admin = mongo.db.users.find_one(
        {"username": username})["admin"]
    if session["user"]:
        return render_template("profile.html", name=name, admin=admin)


@app.route("/sign_out")
def sign_out():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/contact")
def contact():
    if session:
        admin = mongo.db.users.find_one(
          {"username": session["user"]})["admin"]
        name = mongo.db.users.find_one(
          {"username": session["user"]})["first_name"]
        surname = mongo.db.users.find_one(
          {"username": session["user"]})["surname"]
        email = mongo.db.users.find_one(
          {"username": session["user"]})["email"]
        return render_template(
            "contact.html", name=name, surname=surname, email=email,
            admin=admin)

    return render_template("contact.html")


@app.route("/about")
def about():
    if session:
        admin = mongo.db.users.find_one(
          {"username": session["user"]})["admin"]
        return render_template("about.html", admin=admin)

    return render_template("about.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    admin = mongo.db.users.find_one(
          {"username": session["user"]})["admin"]
    genres = list(mongo.db.genres.find())
    if request.method == "POST":
        is_series = "Yes" if request.form.get("series") else "No"
        existing_book = mongo.db.books.find_one(
            {"title": request.form.get("title").lower()}
        )
        if existing_book:
            flash("This book is already in our Library")
            return redirect(url_for("add_book"))
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
                f' {title} has now been added'
                )
            return render_template("add-book.html", genres=genres, admin=admin)
    if session["user"]:
        return render_template("add-book.html", genres=genres, admin=admin)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    genres = list(mongo.db.genres.find())
    if request.method == "POST":
        if mongo.db.users.find_one(
          {"username": session["user"]})["admin"]:
            title = request.form.get("title").lower(),
        else:
            title = mongo.db.books.find_one(
                {"_id": ObjectId(book_id)})["title"]
        is_series = "Yes" if request.form.get("series") else "No"
        update = {
            "title": title,
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
        mongo.db.books.update({"_id": ObjectId(book_id)}, update)
        flash(f"Thankyou {title} has been updated")
        return redirect(url_for("library"))
    if session["user"]:
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        return render_template("edit-book.html", genres=genres, book=book)


@app.route("/delete_book, <book_id>")
def delete_book(book_id):
    title = mongo.db.books.find_one({"_id": ObjectId(book_id)})["title"]
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash(f"{title} Successfully Deleted")
    return redirect(url_for("library"))


@app.route("/manage_genre")
def manage_genre():
    genres = list(mongo.db.genres.find())
    admin = mongo.db.users.find_one(
          {"username": session["user"]})["admin"]
    if admin:
        return render_template(
            "manage_genres.html", genres=genres, admin=admin)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        if mongo.db.users.find_one(
          {"username": session["user"]})["admin"]:
            existing_genre = mongo.db.genres.find_one(
                {"name": request.form.get("name").lower()}
            )
            if existing_genre:
                flash("This genre is already in our collection")
                return redirect(url_for("add_genre"))
            else:
                genre_name = request.form.get("name").lower()
                new_genre = {"name": genre_name}
                mongo.db.genres.insert_one(new_genre)
                flash(
                    f'Thanks { genre_name.title() } is now in our collection')
                return redirect(url_for("manage_genre"))


@app.route("/edit_genre, <genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        genre_name = mongo.db.genres.find_one(
            {"_id": ObjectId(genre_id)})["name"]
        if mongo.db.users.find_one(
          {"username": session["user"]})["admin"]:
            update_genre = {
                "name": request.form.get("name").lower()
                }
            updated_name = request.form.get("name").title()
            mongo.db.genres.update({"_id": ObjectId(genre_id)}, update_genre)
            flash(f"Thankyou { genre_name.title() } has been updated to") + (
                f"{ updated_name }")
            return redirect(url_for("manage_genre"))


@app.route("/delete_genre, <genre_id>")
def delete_genre(genre_id):
    if mongo.db.users.find_one(
          {"username": session["user"]})["admin"]:
        genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})["name"]
        mongo.db.genres.remove({"_id": ObjectId(genre_id)})
        flash(f"{ genre.title() } Successfully Deleted")
        return redirect(url_for("manage_genre"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
