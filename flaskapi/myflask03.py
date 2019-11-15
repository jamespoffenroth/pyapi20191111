#!/usr/bin/python3
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return ("Hello " + guest)

@app.route("/user/<name>")
def hello_user(name):
    # If you go to hello_user with a value of admin
    if name =="admin":
        # Return a 3xx response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # Return a 3xx response to redirect to /guest/<guest>
        return redirect(url_for("hello_guest", guest = name))

if __name__ == "__main__":
    app.run(port=5006)
