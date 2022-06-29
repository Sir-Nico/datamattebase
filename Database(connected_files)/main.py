from ast import dump
from crypt import methods
from multiprocessing import connection
from os import name
import sqlite3

conn = sqlite3.connect('eksempel.db')

c = conn.cursor()

from flask import Flask, request, jsonify, render_template, url_for,redirect, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "hello" 
app.permanent_session_lifetime = timedelta(days =5)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")
    
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash ("Login Succesfull!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged in")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user", methods= ["POST, GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
        return render_template("user.html", email =email)
    else:
        flash( "you are not logged in" )
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug = True)
