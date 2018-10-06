import os

from flask import Flask, session, render_template, request, redirect, url_for
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
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


# pylint: disable=no-member

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    if password != confirmation:
        return render_template("error.html", message="Passwords don't match.")

    db.execute("INSERT INTO users (name, password) VALUES (:name, crypt(:password, gen_salt('md5')))", {"name": name, "password": password})
    db.commit()

    return redirect(url_for('welcome'))

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
    name = request.form.get("name")
    password = request.form.get("password")

    user = db.execute("SELECT * FROM users WHERE name = :name AND password = CRYPT(:password, password)", {"name": name, "password": password}).fetchone()
    if user is None:
        return render_template("error.html", message="Invalid username or password.")
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404