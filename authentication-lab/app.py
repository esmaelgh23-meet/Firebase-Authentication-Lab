from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


const firebaseConfig = {
  apiKey: "AIzaSyAR1N-fr17lyOgRHaPZZBK68_fURX-Eh_4",
  authDomain: "esmael-e2636.firebaseapp.com",
  projectId: "esmael-e2636",
  storageBucket: "esmael-e2636.appspot.com",
  messagingSenderId: "259011972273",
  appId: "1:259011972273:web:b28ef260699a00c2132690",
  measurementId: "G-1WYXG9QVRD"
};

firebase = pyrebase.intitialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)





























