from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from AWSWrapper import Instances

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://brickhack:' + password + '@' + ip + '/brickhack'
db = SQLAlchemy(app)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/EC2/instance/<instance_id>", methods=["GET"])
def instance(instance_id=None):
    instance = Instances.Instances().get_one_instance_info(instance_id)
    return render_template("EC2/instance.html", instance=instance)


@app.route("/EC2/instances", methods=["GET"])
def EC2_instances():
    instances = Instances.Instances().get_all_info()
    return render_template("EC2/instances.html", instances=instances)
