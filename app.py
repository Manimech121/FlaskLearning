from flask import Flask,request,jsonify
import datetime
app = Flask(__name__)
@app.route("/")
def first():
    return "Hello Mani!,How are doing"
@app.route("/ping",methods =['GET'])
def second():
    return "You are doing Good job"