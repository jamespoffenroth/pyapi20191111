#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello {}".format(name)
    ## OLD STYLE STRING FORMATTER - return "Hello %s!" % name

if __name__ == "__main__":
   app.run(port=5006, debug = True)
