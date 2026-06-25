import base64

from flask import Flask,request,jsonify
import datetime
import pickle
import sklearn
app = Flask(__name__)
@app.route("/")
def first():
    return "Hello Mani!,How are doing"
@app.route("/ping",methods =['GET'])
def second():
    return "You are doing Good job"
model = pickle.load(open('classifier.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    input_req = request.get_json()

    gender = 0 if input_req['gender'] == 'Male' else 1
    married = 0 if input_req['married'] == 'Unmarried' else 1
    credit_History = 0 if input_req['credit_History'] == 'Unclear Debts' else 1
    ApplicantIncome = input_req['ApplicantIncome']
    LoanAmount = input_req['LoanAmount']

    features = [[gender, married, ApplicantIncome, LoanAmount, credit_History]]
    prediction = model.predict(features)[0]

    return jsonify({'prediction': int(prediction)})







