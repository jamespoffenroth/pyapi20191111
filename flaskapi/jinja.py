#!/usr/bin/env python3
from flask import Flask, render_template
app = Flask(__name__)

# Grab the value 'username'
@app.route("/<username>")
def index(username):
    # Render the jinja template helloname.html, which applies the value of username to the jinja variable 'name'
    # When user goes to 127.0.0.1:5006/James, the screen will output "Hello James!"
    return render_template("helloname.html", name = username)

if __name__ == "__main__":
    app.run(port=5006)
