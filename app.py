from flask import Flask
from flask import request, render_template, redirect

import os

app = Flask(__name__)

@app.route('/open', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/check_password', methods=['POST'])
def check_password():
    password = os.getenv("DOOR_PASSWORD")
    submitted_password = request.form['pwd']

    if password == submitted_password:
        open_door()
        return "Thanks."
    else:
        return "Nope."

def open_door():
    print("opening door...")
    return True

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run("192.168.0.43")
