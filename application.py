import os

from flask import Flask, session, render_template, request, redirect, url_for, escape
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# for API request
import requests

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

if not os.getenv("API_SECRET_KEY"):
    raise RuntimeError("API_SECRET_KEY is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.urandom(24)
Session(app)

api_key = os.getenv("API_SECRET_KEY")

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# pylint: disable=no-member

@app.route("/", methods=["GET", "POST"])
def index():
    # if a user is logged-in, show search box
    if "user_id" in session:
        return render_template("search.html")
    else:
        return render_template("index.html")

# Sign up
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Get a name and a password from a user
        name = request.form.get("name")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # (additional) server-side confirmation
        if password != confirmation:
            return render_template("error.html", message="Passwords don't match.")

        # query for registration a user into the database
        db.execute("INSERT INTO users (name, password) VALUES (:name, crypt(:password, gen_salt('md5')))",
            {"name": name, "password": password})
        db.commit()

        return redirect(url_for("welcome"))
    else:
        return render_template("signup.html")

# when a new user has signed up
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

# Sign in
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # Get a name and a password from a user
        name = request.form.get("name")
        password = request.form.get("password")

        # query for signing in
        user = db.execute("SELECT * FROM users WHERE name = :name AND password = CRYPT(:password, password)",
            {"name": name, "password": password}).fetchone()

        # if user does not exist in the database, send an error message
        if user is None:
            return render_template("error.html", message="Invalid username or password.")
        else:
            session["user_id"] = db.execute("SELECT id, name FROM users WHERE name = :name AND password = CRYPT(:password, password)",
                {"name": name, "password": password}).fetchone()
            return redirect(url_for("index"))
    else:
        return render_template("signin.html")

# Sign out
@app.route("/signout")
def signout():
    # Remove the user_id from the session if it's there
    if "user_id" in session:
        session.pop("user_id", None)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

# Search location
@app.route("/search", methods=["POST"])
def search():
    # Get a list of locations
    location = '%' + request.form.get("location").upper() + '%'
    results = db.execute("SELECT * FROM locations WHERE zipcode::varchar LIKE :location OR city LIKE :location",
        {"location": location}).fetchall()

    # if no matching location in the database
    if not results:
        return render_template("search.html", message="No locations in the database")

    # if location data exists
    return render_template("search.html", results=results)

# location info
@app.route("/search/<int:location_id>", methods=["GET", "POST"])
def location(location_id):
    if "user_id" in session:
        # if the user submit a comment, commit INSERT query into the database
        if request.method == "POST":
            name = session["user_id"][1]
            comment = request.form.get("comment")
            db.execute("INSERT INTO checkins (name, comment, time, location_id) VALUES (:name, :comment, CURRENT_TIMESTAMP(0), :location_id)",
                {"name": name, "comment": comment, "location_id": location_id})
            db.commit()
        
        # Get the location info and comments
        location = db.execute("SELECT * FROM locations WHERE id = :id",
            {"id": location_id}).fetchone()
        if location is None:
            return render_template("search.html", message="No locations in the database")

        number = db.execute("SELECT COUNT(*) FROM checkins WHERE location_id = :id",
            {"id": location_id}).fetchone()
        comments = db.execute("SELECT * FROM checkins WHERE location_id = :id",
            {"id": location_id}).fetchall()
        return render_template("location.html", location=location, number=number, comments=comments)
    
    # if the user is not logged-in
    return render_template("error.html", message="The requested URL was not found on this server."), 404

# user's comment list
@app.route("/user/<string:name>")
def user(name):
    if session["user_id"][1] == name:
        # Get a list of comments
        number = db.execute("SELECT COUNT(*) FROM checkins WHERE name=:name",
            {"name": name}).fetchone()
        comments = db.execute("SELECT * FROM checkins WHERE name=:name",
            {"name": name}).fetchall()
        if not comments:
            return render_template("comments.html")
    
        return render_template("comments.html", number=number, comments=comments)

    # if the user is not logged-in
    else:
        return render_template("error.html", message="The requested URL was not found on this server."), 404

# If any user tries to access to the nonexistent route, render an error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", message="The requested URL was not found on this server."), 404

if __name__ == "__main__":
    app.run()