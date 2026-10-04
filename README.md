# 📊 Customer Churn Prediction

A machine learning web application that predicts whether a telecom customer is likely to churn based on their demographic information, services, contract details, and billing information.

The project uses a trained machine learning model and a Flask web application to provide real-time churn predictions along with the estimated probability of churn.

---

## 🚀 Project Overview

Customer churn is a major challenge for telecom companies because losing existing customers can directly affect revenue.

This project analyzes customer information and uses machine learning to predict whether a customer is likely to:

- **Stay** with the company
- **Churn** from the company

The trained model is integrated with a Flask web application where users can enter customer details and receive a prediction instantly.

---

## ✨ Features

- Customer churn prediction using Machine Learning
- Interactive Flask web interface
- Real-time prediction
- Churn probability estimation
- Categorical feature encoding
- Pre-trained model integration
- Customer demographic and service information analysis
- Contract and payment information processing

---

## 🧠 Machine Learning Workflow

```text
Customer Dataset
       ↓
Data Cleaning & Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Categorical Encoding
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Serialization
       ↓
Flask Web Application
       ↓
Customer Input
       ↓
Churn Prediction + Probability


## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning & Data Science
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

### Web Development
- Flask
- HTML5
- CSS3

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Python Virtual Environment

### Model Persistence
- Pickle (`.pkl`)

---

## 📊 Dataset

This project uses the **Telco Customer Churn dataset**, which contains information about telecom customers, their services, contracts, and billing details.

### Dataset Features

The dataset contains customer information such as:

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
- Churn

### Target Variable

**Churn** is the target variable.

- `Yes` → Customer is likely to leave the company
- `No` → Customer is likely to stay with the company

---

## 🌐 Web Application

The trained machine learning model is integrated into a **Flask web application**.

The application provides an interactive form where users can enter customer information such as:

- Demographic information
- Customer tenure
- Phone and internet services
- Security and support services
- Contract information
- Billing information
- Payment method

After submitting the form, the application processes the customer information and generates a prediction.

### Application Output

The application displays:

- **Customer churn prediction**
- **Estimated churn probability**

Example:

```text
Customer is likely to STAY

Estimated churn probability: 14.21%
                                    ```

```markdown
---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/bhanu-teja16/customer-churn-prediction.git
cd customer-churn-prediction
                             