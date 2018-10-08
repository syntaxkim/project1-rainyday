import os

from flask import Flask, session, render_template, request, redirect, url_for, escape, Markup
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.urandom(24)
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# pylint: disable=no-member

@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html", message="hello")
    else:
        return render_template("index.html", message=Markup("You need to <a href='/signin'>sign in</a> to use our service."))

# Sign up
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Get a name and a password from a user.
        name = request.form.get("name")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # (additional) server-side confirmation
        if password != confirmation:
            return render_template("error.html", message="Passwords don't match.")

        # query for registration a user into the database
        db.execute("INSERT INTO users (name, password) VALUES (:name, crypt(:password, gen_salt('md5')))", {"name": name, "password": password})
        db.commit()

        return redirect(url_for("welcome"))
    else:
        return render_template("signup.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

# Sign in
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # Get a name and a password from a user.
        name = request.form.get("name")
        password = request.form.get("password")

        # query for signing in
        user = db.execute("SELECT * FROM users WHERE name = :name AND password = CRYPT(:password, password)", {"name": name, "password": password}).fetchone()
        # If user does not exist in the database, send an error message.
        if user is None:
            return render_template("error.html", message="Invalid username or password.")
        else:
            session["username"] = db.execute("SELECT id FROM users WHERE name = :name AND password = CRYPT(:password, password)", {"name": name, "password": password}).fetchone()
            return redirect(url_for("index"))
    else:
        return render_template("signin.html")

# Sign out
@app.route("/signout")
def signout():
    # Remove the user_id from the session if it's there.
    if "username" in session:
        session.pop("username", None)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

# If any user tries to access to the nonexistent route, render an error page.
@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404

if __name__ == "__main__":
    app.run()