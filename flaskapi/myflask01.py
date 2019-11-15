#!/usr/bin/python3

# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class tells the application which URL should call the associated function
# If we receive an HTTP GET to this path, call the hello_world function
# You can have multiple decorators listed that all call the same function
@app.route("/")
def hello_world():
   return "Hello World"

@app.route("/hello/breaktime")
def takeabreak():
    return "I think it is time for a 10 minute break."

# This runs the application. Can be any port, but you want to use a port that is not in use
if __name__ == "__main__":
   app.run(port=5006)
