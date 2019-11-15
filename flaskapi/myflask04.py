#!/usr/bin/python3
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

# This is where we want to redirect users to
@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"

# This is the starting point for users
# Users can land at both / and /start to access postmaker.html
@app.route("/")
@app.route("/start")
def start():
    # Look for templates/postmaker.html
    return render_template("postmaker.html")

# This is where postmaker.html POSTs data to
# A user could also browse (GET) to this location.
@app.route("/login", methods = ["POST", "GET"])
def login():
  # POST would likely come from a user interacting with postmaker.html
  if request.method == "POST":
    # If nm was assigned via the POST
    if request.form.get("nm"):
      # Grab the value of nm from the POST
      user = request.form.get("nm")
    # If the user sent a POST without nm
    else:
      # Then set user equal to defaultuser
      user = "defaultuser"

  # GET would likely come from a user interacting with a browser
  elif request.method == "GET":
    # If nm was assigned as a parameter=value
    if request.args.get("nm"): 
      # Pull nm from localhost:5060/login?nm=larry
      user = request.args.get("nm") 
    # If nm was not passed
    else: 
      # Then set user equal to defaultuser
      user = "defaultuser" 
    # Pass back to /success with value for name
  return redirect(url_for("success", name = user)) 

if __name__ == "__main__":
    app.run(port=5006)
