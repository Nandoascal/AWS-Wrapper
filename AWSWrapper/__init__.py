from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://brickhack:' + password + '@' + ip + '/brickhack'
db = SQLAlchemy(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
