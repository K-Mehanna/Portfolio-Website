import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology

from cs50 import SQL
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///contact.db")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/vert", methods=["GET", "POST"])
def vert():
    if request.method == "GET":
        return render_template("vert.html")
        

    else:
        forename = request.form.get("forename")
        surname = request.form.get("surname")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        if not forename:
            return apology("Must provide a forename")

        elif not surname:
            return apology("Must provide a surname")
        
        elif not email:
            return apology("Must provide an email")

        elif not subject:
            return apology("Must provide a subject")

        elif not message:
            return apology("Must provide a message")

        db.execute("INSERT INTO messages (Forename, Surname, Email, Subject, Message) VALUES (:forename, :surname, :email, :subject, :message);", forename=forename, surname=surname, email=email, subject=subject, message=message)

        flash("Message sent")
        return redirect("/vert")


@app.route("/animated")
def animated():
    return render_template("animated.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
