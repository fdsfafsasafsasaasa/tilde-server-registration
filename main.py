from types import MethodDescriptorType
from flask import Flask, render_template, flash, request, redirect
from utils import check_username, create_user

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")
    
    
@app.route("/create", methods=["POST"])
def create():
    user = request.form.to_dict()
    if not check_username(user['username']):
        return
    else:
        print(user)
        create_user(user['username'], user['password'], user['sshkey'])
        return redirect("/thanks")
    
@app.route("/thanks")
def thanks():
    return render_template("result.html")

app.run()