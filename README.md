# Customer Churn Prediction

## Project Overview

A machine learning-based web application that predicts whether a customer is likely to churn or stay.

Users can enter customer information through an interactive web interface and receive a churn prediction along with an estimated churn probability.

## Features

- Customer churn prediction
- Interactive web-based interface
- Machine learning model integration
- Categorical feature encoding
- Churn probability estimation
- Flask-based web application
- Responsive user interface

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Flask
- HTML
- CSS

## Input Features

The application uses customer information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

## Machine Learning

The trained machine learning model is saved using Joblib and loaded by the Flask application.

The application performs the following steps:

1. Collects customer information from the web form.
2. Converts numerical values into the required format.
3. Applies the saved categorical encoders.
4. Arranges the input features in the same order used during training.
5. Sends the processed data to the trained model.
6. Generates a churn prediction.
7. Calculates the estimated churn probability.
8. Displays the result on the web interface.

## Project Structure

```text
customer-churn-prediction/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── customer_churn_model.pkl
│   ├── feature_columns.pkl
│   └── label_encoders.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── README.md
└── requirements.txt 
                     ```