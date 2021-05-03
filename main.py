from types import MethodDescriptorType
from flask import Flask, render_template, flash, request, redirect
from utils import check_username, create_user

app = Flask(__name__)

app.secret_key = "you'llneverguessthis;)"

with open("/etc/shells", "r") as temp:
    shells = temp.read().rstrip().split("\n")
    del shells[0]

@app.route("/")
def root():
    return render_template("index.html", shells=shells)
    
@app.route("/create", methods=["POST"])
def create():
    user = request.form.to_dict()
    check = check_username(user['username'])
    if not check[0]:
        flash("There has been an error with your application")
        flash(check[1])
    else:
        created_user = create_user(user['username'], user['password'], user['sshkey'], user['shell'])
        if not created_user[0]:
            flash("There has been an error with your application")
            flash(created_user[1])
            
    return redirect("/thanks")
    
@app.route("/thanks")
def thanks():
    return render_template("result.html")

app.run()