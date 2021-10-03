# imports
import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_paginate import Pagination, get_page_args
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# configurations
app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


# admin function to find users admin status
def admin():
    admin = mongo.db.users.find_one(
        {"username": session["user"]})["admin"]
    return admin


# genres function to find all current genre documents
def genres():
    genres = mongo.db.genres.find()
    return genres


# "library" view
@app.route("/")
@app.route("/library")
def library():
    # Find all books
    books = list(mongo.db.books.find())

    # Pagination, code mostly from
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    def get_books(offset=0, per_page=5):
        offset = page * per_page - per_page
        return books[offset: offset + per_page]

    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    per_page = 5
    pagination_books = get_books(offset=offset, per_page=per_page)
    pagination = Pagination(
        page=page, per_page=per_page, total=len(books),
        css_framework='bootstrap4')
    # If a user is logged in then admin will be passed
    # into template as well.
    if session:
        return render_template('library.html', admin=admin(),
                               books=pagination_books, page=page,
                               per_page=per_page, pagination=pagination)
    return render_template('library.html', books=pagination_books, page=page,
                           per_page=per_page, pagination=pagination)


# "search_library" view, gets user input from search box and looks
# for a match in the db.
@app.route("/search_library", methods=["GET", "POST"])
def search_library():
    if request.method == "POST":
        search = request.form.get("search").lower()
        results = list(mongo.db.books.find(
            {"$text": {"$search": search}}))

        # Pagination, code mostly from
        # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
        def get_books(offset=0, per_page=5):
            offset = page * per_page - per_page
            return results[offset: offset + per_page]

        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page')
        per_page = 5
        pagination_results = get_books(offset=offset, per_page=per_page)
        pagination = Pagination(
            page=page, per_page=per_page, total=len(results),
            css_framework='bootstrap4')
        # If there are results then check whether user logged in
        # to determine whether admin needs passed in or not.
        if results:
            if session:
                return render_template(
                    "library.html", admin=admin(), results=pagination_results,
                    page=page, per_page=per_page, pagination=pagination)
            else:
                return render_template(
                    "library.html", results=pagination_results, page=page,
                    per_page=per_page, pagination=pagination)
        # If there are no results then display flash message.
        else:
            flash(f"Sorry cannot find { search.title()}")
            return redirect(url_for("library"))


# "register" view
@app.route("/register", methods=["GET", "POST"])
def register():
    # If registration form submitted check whether username already taken
    if request.method == "POST":
        existing = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # If username taken display flash message and reload page.
        if existing:
            flash(
                "Username is taken, try adding numbers or choose",
                "another username"
                )
            return redirect(url_for("register"))
        # If password and confirmation password don't match
        # display flash message and reload page.
        if request.form.get("password") != request.form.get(
                "confirm-password"):
            flash("Your passwords did not match, please try again")
            return redirect(url_for("register"))
        # Get information for new user from registration form
        register_user = {
            "first_name": request.form.get("first_name"),
            "surname": request.form.get("surname"),
            "email": request.form.get("email"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "genre": request.form.get("genre"),
            "admin": bool("")
        }
        # New user created in db
        mongo.db.users.insert_one(register_user)
        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # Create users profile document in db
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        mongo.db.profiles.insert_one({
            "user_id": ObjectId(user_id),
            "books_to_read": [],
            "own_books": [],
            "read_books": []})
        # Display personalised message and load profile page.
        name = request.form.get("first_name")
        flash(
            f'Welcome {name} ' +
            'you have been successfully registered.')
        return redirect(url_for("profile", username=session["user"]))
    # Use register.html template, passing in genres.
    return render_template("register.html", genres=genres())


# "sign_in" view
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    # When user submits sign in form check that username exists
    if request.method == "POST":
        existing = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        # If username exists use function from werkzeug.security to check
        # password matches username
        if existing:
            if check_password_hash(
              existing["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session["user"]))
            # If password not correct display flash message
            else:
                flash("Your information did not match our records " +
                      "please try again, or contact us for help.")
                return redirect(url_for("sign_in"))
        # If username doesn't exist display flash message.
        else:
            flash("Your information did not match our records " +
                  "please try again, or contact us for help.")
            return redirect(url_for("sign_in"))
    # Use sign_in.html template
    return render_template("sign-in.html")


# "profile" view
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Get users username from db to pass into template
    name = mongo.db.users.find_one(
        {"username": username})["first_name"]
    # If user logged in get profile information to pass into template
    if session["user"]:
        user_id = mongo.db.users.find_one(
            {"username": session["user"]})["_id"]
        user_profile = mongo.db.profiles.find_one(
            {"user_id": ObjectId(user_id)})
        read_books = mongo.db.profiles.find_one(
            {"user_id": ObjectId(user_id)})["read_books"]
        own_books = user_profile["own_books"]
        books_to_read = user_profile["books_to_read"]
        # Use profile.html template passing in required variables
        return render_template(
            "profile.html", name=name, admin=admin(), read_books=read_books,
            own_books=own_books, books_to_read=books_to_read)


# "profile_add" view for adding books from library to profile
@app.route("/profile_add, <book_id>", methods=["GET", "POST"])
def profile_add(book_id):
    # Get info from database and store in variables
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    book = mongo.db.books.find_one(
        {"_id": ObjectId(book_id)})
    book_title = mongo.db.books.find_one(
        {"_id": ObjectId(book_id)})["title"]
    # If form submitted get information from fields
    if request.method == "POST":
        read = request.form.get("read")
        own = request.form.get("own")
        # If book owned and has been read by user then book
        # will be added to both read_books and own_books arrays
        if own and read:
            update = mongo.db.profiles.update(
              {"user_id": ObjectId(user_id)},
              {"$addToSet": {"own_books": book_title}}
            ), mongo.db.profiles.update(
              {"user_id": ObjectId(user_id)},
              {"$addToSet": {"read_books": book_title}}
            )
            # Display flash confirmation message and redirect to library
            if update:
                flash("Great thats been added to your profile")
                return redirect(url_for("library"))
        # If book not owned but read by user, add
        # book to read_books array.
        elif not own and read:
            update = mongo.db.profiles.update(
              {"user_id": ObjectId(user_id)},
              {"$addToSet": {"read_books": book_title}}
            )
            # Display flash confirmation message and redirect to library
            if update:
                flash("Great thats been added to your profile")
                return redirect(url_for("library"))
        # If book owned but not read by user, add
        # book to books_to_read and own_books array.
        elif own and not read:
            update = mongo.db.profiles.update(
              {"user_id": ObjectId(user_id)},
              {"$addToSet": {"books_to_read": book_title}}
            ), mongo.db.profiles.update(
              {"user_id": ObjectId(user_id)},
              {"$addToSet": {"own_books": book_title}}
            )
            # Display flash confirmation message and redirect to library
            if update:
                flash("Great thats been added to your profile")
                return redirect(url_for("library"))
        # If book not read or owned add to books_to_read array
        else:
            update = mongo.db.profiles.update(
              {"user_id": ObjectId(user_id)},
              {"$addToSet": {"books_to_read": book_title}}
            )
            # Display flash confirmation message and redirect to library
            if update:
                flash("Great thats been added to your profile")
                return redirect(url_for("library"))
    # Use profile add template passing in required variables
    if session["user"]:
        return render_template(
            "profile-add.html", admin=admin(), book=book)


# "not_read" view, to move book from read_books to books_to_read
# array in profile
@app.route("/not_read, <book>", methods=["GET", "POST"])
def not_read(book):
    # Get user_id of user to find profile
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    # Update profile by deleting book from read_books
    # and add to books_to_read array
    update = mongo.db.profiles.update(
        {"user_id": ObjectId(user_id)},
        {"$pull": {"read_books": book}}),
    mongo.db.profiles.update(
        {"user_id": ObjectId(user_id)},
        {"$addToSet": {"books_to_read": book}})
    # Display flash confirmation message and redirect to profile
    if update:
        flash(f"Thats {book} moved to the books to read bookshelf")
        return redirect(url_for("profile", username=session["user"]))


# "books_read_delete" view to delete book from read_books
@app.route("/books_read_delete, <book>", methods=["GET", "POST"])
def books_read_delete(book):
    # Get user_id of user to find profile
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    # Update profile
    update = mongo.db.profiles.update(
        {"user_id": ObjectId(user_id)},
        {"$pull": {"read_books": book}})
    # Display flash confirmation message and redirect to profile
    if update:
        flash(f"Thats {book} removed.")
        return redirect(url_for("profile", username=session["user"]))


# "own_books_add" view is for updating profile books that weren't
# owned when initially added to profile.
@app.route("/own_book_add, <book>", methods=["GET", "POST"])
def own_book_add(book):
    # Get user_id of user to find profile
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    # Update profile by adding book to own_books array
    update = mongo.db.profiles.update(
        {"user_id": ObjectId(user_id)},
        {"$addToSet": {"own_books": book}})
    # Display flash confirmation message and redirect to profile
    if update:
        flash(f"Thats {book} added to own books.")
        return redirect(url_for("profile", username=session["user"]))


# "books_to_read_delete" view is for deleting books from
# books_to_read array
@app.route("/books_to_read_delete, <book>", methods=["GET", "POST"])
def books_to_read_delete(book):
    # Get user_id of user to find profile
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    # Update profile by deleting book from books_to_read array
    update = mongo.db.profiles.update(
        {"user_id": ObjectId(user_id)},
        {"$pull": {"books_to_read": book}})
    # Display flash confirmation message and redirect to profile
    if update:
        flash(f"Thats {book} removed.")
        return redirect(url_for("profile", username=session["user"]))


# "read_book" view is for moving a book from books_to_read
# array to read_book array
@app.route("/read_book, <book>", methods=["GET", "POST"])
def read_book(book):
    # Get user_id of user to find profile
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    # Update profile by deleting book from books_to_read array
    # and adding to read_books array
    update = mongo.db.profiles.update(
        {"user_id": ObjectId(user_id)},
        {"$pull": {"books_to_read": book}}),
    mongo.db.profiles.update(
        {"user_id": ObjectId(user_id)},
        {"$addToSet": {"read_books": book}})
    # Display flash confirmation message and redirect to profile
    if update:
        flash(f"Thats {book} moved to the read bookshelf")
        return redirect(url_for("profile", username=session["user"]))


# "own_book_delete" view to delete book from own_books
@app.route("/own_book_delete, <book>", methods=["GET", "POST"])
def own_book_delete(book):
    # Get user_id of user to find profile
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    # Update profile
    update = mongo.db.profiles.update(
        {"user_id": ObjectId(user_id)},
        {"$pull": {"own_books": book}})
    # Display flash confirmation message and redirect to profile
    if update:
        flash(f"Thats {book} removed.")
        return redirect(url_for("profile", username=session["user"]))


# "sign_out" view to end users session, display message
# and redirect to sign in
@app.route("/sign_out")
def sign_out():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("sign_in"))


# "contact" view to display contact template
@app.route("/contact")
def contact():
    # if user logged in user info passed in with template to prefill
    # contact form
    if session:
        name = mongo.db.users.find_one(
          {"username": session["user"]})["first_name"]
        surname = mongo.db.users.find_one(
          {"username": session["user"]})["surname"]
        email = mongo.db.users.find_one(
          {"username": session["user"]})["email"]
        return render_template(
            "contact.html", name=name, surname=surname, email=email,
            admin=admin())
    return render_template("contact.html")


# "about" view to display about template
@app.route("/about")
def about():
    # if user logged in admin status passed in with template
    if session:
        return render_template("about.html", admin=admin())
    return render_template("about.html")


# "add_book" view to add book to library
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    # if add_book form submitted get information from form
    if request.method == "POST":
        # If title stripped of spaces is empty then display
        # flash message and reload add_book form
        if not request.form.get("title").strip():
            flash("Please provide a title")
            return redirect(url_for('add_book'))
        # If title supplied then get information from form
        else:
            is_series = "Yes" if request.form.get("series") else "No"
            # Check if book already exists in database
            existing_book = mongo.db.books.find_one(
                {"title": request.form.get("title").lower()}
            )
            # If book exists, display message and reload add_book
            if existing_book:
                flash("This book is already in our Library")
                return redirect(url_for("add_book"))
            # Insert new book, display message and redirect to library
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
                    f' {title} has now been added')
                return redirect(url_for("library"))
    # Use add_book template, passing in admin and genre
    if session["user"]:
        return render_template("add-book.html", genres=genres(), admin=admin())


# "edit_book" view to edit books in library
@app.route("/edit_book, <book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    # if edit_book form submitted get information from form
    if request.method == "POST":
        # if admin get title from form otherwise from the book document
        if admin:
            title = request.form.get("title").lower()
        else:
            title = mongo.db.books.find_one(
                {"_id": ObjectId(book_id)})["title"]
        # update document with information from form, display message and
        # redirect to library
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
        flash(f"Thankyou {title.title()} has been updated")
        return redirect(url_for("library"))
    # Check user is logged in before using edit_book template and pass
    # in genre, book and admin variables
    if session["user"]:
        book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        return render_template(
            "edit-book.html", genres=genres(), book=book, admin=admin())


# "delete_book" view to delete book from library
@app.route("/delete_book, <book_id>")
def delete_book(book_id):
    # Delete book, display message and reload library
    title = mongo.db.books.find_one({"_id": ObjectId(book_id)})["title"]
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash(f"{title} Successfully Deleted")
    return redirect(url_for("library"))


# "manage_genre" view to see all current genres
@app.route("/manage_genre")
def manage_genre():
    # if user is an admin use manage_genres template
    if admin():
        return render_template(
            "manage-genres.html", genres=genres(), admin=admin)


# "add_genre" view to add genre
@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    # if form submitted get info from form field
    if request.method == "POST":
        # Check user is admin
        if mongo.db.users.find_one(
          {"username": session["user"]})["admin"]:
            # Check genre doesn't already exist in database
            existing_genre = mongo.db.genres.find_one(
                {"name": request.form.get("name").lower()}
            )
            # If genre already exists display message and refresh form
            if existing_genre:
                flash("This genre is already in our collection")
                return redirect(url_for("add_genre"))
            # If genre doesn't exist insert new genre document, display
            # message and reload manage_genre
            else:
                genre_name = request.form.get("name").lower()
                new_genre = {"name": genre_name}
                mongo.db.genres.insert_one(new_genre)
                flash(
                    f'Thanks { genre_name.title() } is now in our collection')
                return redirect(url_for("manage_genre"))


# "edit_genre" view to edit current genres
@app.route("/edit_genre, <genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    # if form submitted get info from field form
    if request.method == "POST":
        genre_name = mongo.db.genres.find_one(
            {"_id": ObjectId(genre_id)})["name"]
        # if user is admin update genre, display message
        # and reload manage_genre page.
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


# "delete_genre" view to delete a genre document from database
@app.route("/delete_genre, <genre_id>")
def delete_genre(genre_id):
    # if user an admin then delete genre, display message
    # and reload manage_genre.
    if mongo.db.users.find_one(
          {"username": session["user"]})["admin"]:
        genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})["name"]
        mongo.db.genres.remove({"_id": ObjectId(genre_id)})
        flash(f"{ genre.title() } Successfully Deleted")
        return redirect(url_for("manage_genre"))


# "manage_users" view to allow admin to view current users
@app.route("/manage_users")
def manage_users():
    # Assign data from database to variables to send into template
    users = mongo.db.users.find()
    # if user is an admin use manage_users template
    if admin():
        return render_template(
            "manage-users.html", users=users, admin=admin)


# "search_users" view to search current users by admin
@app.route("/search_users", methods=["GET", "POST"])
def search_users():
    # Check if user is an admin
    if admin():
        # If form submitted get info from form fields
        if request.method == "POST":
            # if search is for admin, find all users that are admin
            # and assign to results variable and pass in with template
            search = request.form.get("search").lower()
            if search == "admin":
                results = list(mongo.db.users.find(
                    {"admin": bool("true")})
                )
                return render_template(
                    "manage-users.html", results=results, admin=admin)
            # If search is not for admin then search database for usernames
            # matching input from user.
            elif search:
                results = list(mongo.db.users.find(
                    {"username": search}))
                # If there is a result pass into template
                if results:
                    return render_template(
                        "manage-users.html", results=results, admin=admin)
                # If there isn't a result display message and reload page
                else:
                    flash(f"Sorry couldn't find {search}")
                    return redirect(url_for("manage_users"))


# "edit_user" view to edit users information by admin
@app.route("/edit_user, <user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    # When form is submitted get information from fields
    if request.method == "POST":
        username = mongo.db.users.find_one(
            {"_id": ObjectId(user_id)})["username"]
        is_admin = bool("true") if request.form.get("admin") else bool("")
        # If password and confirm password don't match, display message
        # and refresh form
        if request.form.get("password") != request.form.get(
                "confirm-password"):
            flash("Your passwords did not match, please try again")
            return redirect(url_for("edit_user"))
        # If password filled in, update three fields in the document
        # display message and reload page
        if request.form.get("password"):
            update_user = {
                "email": request.form.get("email"),
                "admin": is_admin,
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.update(
                {"_id": ObjectId(user_id)}, {"$set": update_user})

            flash(f"Thankyou {username} has been updated,") + (
                "email them with their new password")
            return redirect(url_for("manage_users"))
        # If password not needing updated, update two fields in the document
        # display message and reload page
        else:
            update_user = {
                "email": request.form.get("email"),
                "admin": is_admin
            }
            mongo.db.users.update(
                {"_id": ObjectId(user_id)}, {"$set": update_user})

            flash(f"Thankyou {username} has been updated")
            return redirect(url_for("manage_users"))
    # If admin use edit_user template
    if admin():
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return render_template("edit-user.html", user=user, admin=admin)


# "delete_user" view to delete users account by admin
@app.route("/delete_user, <user_id>")
def delete_user(user_id):
    username = mongo.db.users.find_one(
          {"_id": ObjectId(user_id)})["username"]
    # If admin delete user, display message and reload page
    if admin():
        mongo.db.profiles.remove({"user_id": ObjectId(user_id)})
        mongo.db.users.remove({"_id": ObjectId(user_id)})
        flash(f"{ username } Successfully Deleted")
        return redirect(url_for("manage_users"))


# "edit_account" view for user to edit their information
@app.route("/edit_account", methods=["GET", "POST"])
def edit_account():
    # Get information from db and assign to variables
    user = mongo.db.users.find_one(
          {"username": session["user"]})
    # If form submitted get information from form fields
    if request.method == "POST":
        # If password and confirm_password don't match display message
        if request.form.get("password") != request.form.get(
                "confirm-password"):
            flash("Your passwords did not match, please try again")
            return redirect(url_for("edit_account"))
        # Check password matches username
        if request.form.get("password"):
            if check_password_hash(
               user["password"], request.form.get("current-password")):
                # If password and confirm password don't match display
                # message and reload page
                if request.form.get("password") != request.form.get(
                  "confirm-password"):
                    flash("Your passwords did not match, please try again")
                    return redirect(url_for("edit_account"))
                # If password matches username update 5 fields, display
                # message and redirect to profile
                else:
                    update_user = {
                        "first_name": request.form.get("first_name"),
                        "surname": request.form.get("surname"),
                        "email": request.form.get("email"),
                        "genre": request.form.get("genre"),
                        "password": generate_password_hash(
                            request.form.get("password"))
                    }
                    mongo.db.users.update(user, {"$set": update_user})

                    flash("Thankyou that's been updated")
                    return redirect(url_for(
                        "profile", username=session["user"]))
            # If password doesn't match that in user document display
            # message and reload page
            else:
                flash("Your information did not match our records " +
                      "please try again.")
                return redirect(url_for("edit_account"))
        # If password not filled in, update four fields in the document
        # display message and reload page
        else:
            update_profile = {
                "first_name": request.form.get("first_name"),
                "surname": request.form.get("surname"),
                "email": request.form.get("email"),
                "genre": request.form.get("genre")
            }
            mongo.db.users.update(
                user, {"$set": update_profile})
            flash("Thankyou that's been updated")
            return redirect(url_for("profile", username=session["user"]))
    # If user logged in use edit_account template, passing in variables
    if session["user"]:
        return render_template(
            "edit-account.html", user=user, admin=admin(), genres=genres())


# "delete_account" view allows users to delete their own account
@app.route("/delete_account")
def delete_account():
    # Delete user, end session, display messsage and redirect to library
    user_id = mongo.db.users.find_one(
          {"username": session["user"]})["_id"]
    mongo.db.profiles.remove({"user_id": ObjectId(user_id)})
    mongo.db.users.remove({"username": session["user"]})
    session.pop("user")
    flash("Account Successfully Deleted, We're sorry to see you go.")
    return redirect(url_for("library"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
