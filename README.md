# Loan Prediction Web App

A Flask-based machine learning web application that predicts whether a loan is likely to be approved or rejected based on user input such as gender, marital status, credit history, applicant income, and loan amount.

## Project Overview

This project demonstrates how to deploy a machine learning classification model using Flask and provide a simple browser-based interface for user interaction. The application collects user input through an HTML form, processes the inputs in Python, passes them to a trained model, and displays the prediction result on the web page.

## Features

- User-friendly web interface built with HTML and CSS
- Flask backend for handling routes and form submission
- Machine learning model loaded using pickle
- Real-time prediction from browser input
- Colorful and responsive form design

## Tech Stack

- Python
- Flask
- HTML
- CSS
- Scikit-learn
- Pickle

## Project Structure

```bash
Loan-Prediction-Web-App/
│
├── app.py
├── classifier.pkl
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## How It Works

1. The user opens the home page in the browser.
2. Flask renders the `index.html` file.
3. The user enters the required loan details in the form.
4. The form sends the data to the `/predict` route using a POST request.
5. Flask reads the submitted values using `request.form`.
6. The input values are converted into numerical format for the model.
7. The trained model predicts whether the loan is approved or rejected.
8. Flask sends the result back to the same HTML page.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows
```bash
venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask app

```bash
python app.py
```

### 6. Open in browser

```text
http://127.0.0.1:5000/
```

## Example Input

- Gender: Male
- Marital Status: Married
- Credit History: Clear Debts
- Applicant Income: 5000
- Loan Amount: 150000

## Example Output

- Loan Approved  
or  
- Loan Rejected

## Future Improvements

- Add more input features for better prediction
- Improve input validation and error handling
- Deploy the application on Render, Railway, or Heroku
- Add model evaluation metrics in the UI
- Replace pickle with a more production-ready deployment pipeline

## Learning Outcome

This project helped in understanding:
- Flask routing
- HTML form handling
- Connecting frontend with backend
- Loading and using machine learning models in web apps
- Basic deployment workflow for ML applications

## Author

**Mani Kandan**  
Data Science Learner | Python | Machine Learning | Flask

## License

This project is for learning and portfolio purposes.
