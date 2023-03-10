from flask import Flask, request, render_template, redirect, session
from flask_session import Session
import helper as ffw

app = Flask(__name__)
# configure app to use sessions
app.config["SESSION_PERMANT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# to set session variables --> session["varname"] = value
# to get session variables --> session.get("varname") or session["varname"]
# to "clear" session variables --> session["varname"] = None

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "GET": # they clicked the link/button
    return render_template("login.html")
  else: # filled out the login form
    # get the email from the form
    email = request.form.get("member_email")
    # load the current members
    MEMBERS = ffw.load_members()
    # loop throug the members and see if the email matches
    for member in MEMBERS:
      if member.get("email") == email:
        #set the logged_in session variable
        session["logged_in"] = True
        session["cur_member"] = member
        return redirect("/")
    #email did not match any users
    return redirect("/login")

@app.route("/logout")
def logout():
  # clear out all session variables and go back to the home page
  session["logged_in"] = None
  return redirect("/")

if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
