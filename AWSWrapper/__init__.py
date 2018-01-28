from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from AWSWrapper import Instances, Instance

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://brickhack:' + password + '@' + ip + '/brickhack'
db = SQLAlchemy(app)


@app.route("/setIAMRole/<instance_id>", methods=['POST'])
def setIAMRole(instance_id=None):
    return jsonify({"result": "success"})


@app.route("/setScaling/<instance_id>", methods=['POST'])
def setScaling(instance_id=None):
    return jsonify({"result": "success"})


@app.route("/setType/<instance_id>", methods=['POST'])
def setType(instance_id=None):
    return jsonify({"result": "success"})


@app.route("/setTermination/<instance_id>", methods=['POST'])
def setTermination(instance_id=None):
    return jsonify({"result": "success"})


@app.route("/setUserData/<instance_id>", methods=['POST'])
def setUserData(instance_id=None):
    return jsonify({"result": "success"})


@app.route("/setModifyInstance/<instance_id>", methods=['POST'])
def setModifyInstance(instance_id=None):
    return jsonify({"result": "success"})


@app.route("/setNewInstance/<image_id>", methods=['POST'])
def setNewInstance(image_id):
    Instances.Instances().launch_instance(image_id)
    return jsonify({"result": "success"})


@app.route("/setStart/<instance_id>", methods=['POST'])
def setStart(instance_id=None):
    Instance.Instance(instance_id).turn_on()
    return jsonify({"result": "success"})


@app.route("/setStop/<instance_id>", methods=['POST'])
def setStop(instance_id=None):
    Instance.Instance(instance_id).turn_off()
    return jsonify({"result": "success"})


@app.route("/setReboot/<instance_id>", methods=['POST'])
def setReboot(instance_id=None):
    Instance.Instance(instance_id).reboot()
    return jsonify({"result": "success"})


@app.route("/setKill/<instance_id>", methods=['POST'])
def setKill(instance_id=None):
    Instance.Instance(instance_id).terminate()
    return jsonify({"result": "success"})


@app.route("/setDownCreateImage/<instance_id>", methods=['POST'])
def setDownCreateImage(instance_id=None):
    return jsonify({"result": "success"})


@app.route("/setDownBundleInstance/<instance_id>", methods=['POST'])
def setDownBundleInstance(instance_id=None):
    return jsonify({"result": "success"})


@app.route("/setT2/<instance_id>", methods=["POST"])
def setT2(instance_id=None):
    return jsonify({"result": "success"})


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/EC2/instance/<instance_id>", methods=["GET"])
def instance(instance_id=None):
    instance = Instance.Instance(instance_id).get_info()
    return render_template("EC2/instance.html", instance=instance)


@app.route("/EC2/instances", methods=["GET"])
def EC2_instances():
    instances = Instances.Instances().get_all_info()
    return render_template("EC2/instances.html", instances=instances)
