from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://brickhack:' + password + '@' + ip + '/brickhack'
db = SQLAlchemy(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/EC2/instance", methods=["GET"])
def instance():
    return render_template("EC2/instance.html")

@app.route("/EC2/instances", methods=["GET"])
def EC2_instances():
    instances = [{'name': 'test1', 'state': 'running'}, {'name': 'test2', 'state': 'pending'},
                 {'name': 'test3', 'state': 'shutting-down'}, {'name': 'test4', 'state': 'stopped'},
                 {'name': 'test5', 'state': 'terminated'}]
    return render_template("EC2/instances.html", instances=instances)
