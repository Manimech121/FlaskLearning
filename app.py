from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('classifier.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender_input = request.form.get('gender')
        married_input = request.form.get('married')
        credit_input = request.form.get('credit_History')
        applicant_income = float(request.form.get('ApplicantIncome'))
        loan_amount = float(request.form.get('LoanAmount'))

        gender = 0 if gender_input == 'Male' else 1
        married = 0 if married_input == 'Unmarried' else 1
        credit_History = 0 if credit_input == 'Unclear Debts' else 1

        features = [[gender, married, applicant_income, loan_amount, credit_History]]
        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "Loan Approved"
            result_class = "approved"
        else:
            result = "Loan Rejected"
            result_class = "rejected"

        return render_template('index.html', prediction_text=result, result_class=result_class)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", result_class="error")

if __name__ == '__main__':
    app.run(debug=True)