from flask import Flask, flash, request, redirect, url_for, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.request import urlopen
import json
import requests
from dash_application import create_dash_application


app = Flask(__name__)
app.config["SECRET_KEY"] = "so,secret"
ALLOWED_HOSTS = ['.herokuapp.com']
create_dash_application(app)


# ---------------------------------------- No Route ---------------------------------------- ##
@app.route("/")
def index():
    return render_template("home.html", message="Log-In")

# ---------------------------------------- Login ---------------------------------------- #
@app.route("/login", methods=["POST"])
def login():
    # 1. get the form from the request
    username = request.form["username"]
    password = request.form["password"]
    if username == "" or password == "":
        return render_template("home.html", message = "Please.")

    # 2. Fetch Data from DB
    url = f"https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/user_password/{username}"
    user_data = json.loads(urlopen(url).read())['items']

    # 3. Validate user and password combination
    # 3.1 Return Empty --> User unknown
    if user_data == []:
        return render_template("home.html", message = "Unknown user.")
    # 3.2 Password correct
    elif check_password_hash(user_data[0]['password'], password):
        session["username"] = username
        return redirect('/dash/')
    # 3.3 Password incorrect
    else:
        return render_template("home.html", message = "Wrong Password.")

# ---------------------------------------- Registration ---------------------------------------- #
@app.route("/register")
def register():
    return render_template("register_form.html", text_register = 'Register New User:')

@app.route("/re_register")
def forgot_password():
    return render_template("register_form.html", text_register = 'Create New Password:')

@app.route("/create_new_user", methods=["POST"])
def create_new_user():
    # 1. Collect the data from the form
    username = request.form["username"]
    password = request.form["password"]
    password_confirmed = request.form["password_confirmed"]
    
    # 2. Make Sure Email is from iberia or ie
    if 'iberia' in username or 'ie' in username:
        # 2.1 Confirm that password matches
        # 2.1.1 If match, create user in db and log user in
        if password == password_confirmed:
            hashed_password = generate_password_hash(password)
            url = "https://gb5f03b1d0c0d8d-tiptombers2021.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/createuser/users/"
            requests.post(url, data={"username": username, "password": hashed_password})
            session["username"] = username
            return redirect('/dash/')
        # 2.1.2 When password don't match, re-render and inform
        else:
            return render_template("register_form.html", text_register = 'Error: Passwords did not match')
    # 3. If Iberia or IE not in username
    else:
        return render_template("register_form.html", text_register='Unauthorised user')

# ---------------------------------------- Dashboard ---------------------------------------- #
@app.route("/dash/")
def to_dashboard():
    if "username" in session:
        create_dash_application(app)
    else:
        return render_template("home.html", message="Log-In")


# ---------------------------------------- Logout ---------------------------------------- #
@app.route("/to_logout")
def to_logout():
    if "username" in session:
        session.pop("username")
        return render_template("logout.html")
    else: 
        return render_template("home.html", message="Log-In")

# ---------------------------------------- The End ---------------------------------------- #

