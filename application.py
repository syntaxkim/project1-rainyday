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
    return redirect(url_for('index'))
