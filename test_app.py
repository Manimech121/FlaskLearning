import importlib
import sys
from unittest.mock import Mock, patch
import pytest


@pytest.fixture
def app_module():
    fake_model = Mock()
    fake_model.predict.return_value = [1]

    if "app" in sys.modules:
        del sys.modules["app"]

    with patch("pickle.load", return_value=fake_model):
        module = importlib.import_module("app")
        module.app.config["TESTING"] = True
        module.fake_model = fake_model
        yield module


@pytest.fixture
def client(app_module):
    with app_module.app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_predict_approved(client, app_module):
    app_module.fake_model.predict.return_value = [1]

    response = client.post("/predict", data={
        "gender": "Male",
        "married": "Married",
        "credit_History": "Clear Debts",
        "ApplicantIncome": "5000",
        "LoanAmount": "200"
    })

    assert response.status_code == 200
    assert b"Loan Approved" in response.data


def test_predict_rejected(client, app_module):
    app_module.fake_model.predict.return_value = [0]

    response = client.post("/predict", data={
        "gender": "Female",
        "married": "Unmarried",
        "credit_History": "Unclear Debts",
        "ApplicantIncome": "3000",
        "LoanAmount": "15"
    })

    assert response.status_code == 200
    assert b"Loan Rejected" in response.data


def test_predict_invalid_input(client):
    response = client.post("/predict", data={
        "gender": "Male",
        "married": "Married",
        "credit_History": "Clear Debts",
        "ApplicantIncome": "abc",
        "LoanAmount": "200"
    })

    assert response.status_code == 200
    assert b"Error:" in response.data