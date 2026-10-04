from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load saved model and preprocessing files
model = joblib.load("notebooks/customer_churn_model.pkl")
print("Model classes:", model.classes_)

feature_columns = joblib.load("notebooks/feature_columns.pkl")
encoders = joblib.load("notebooks/label_encoders.pkl")

print("Encoder columns:", list(encoders.keys()))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from the form
    customer_data = {}

    for feature in feature_columns:
        customer_data[feature] = request.form.get(feature)

    # Convert numeric columns
    numeric_columns = [
        "SeniorCitizen",
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    for col in numeric_columns:
        if col in customer_data:
            customer_data[col] = float(customer_data[col])

    # Convert categorical columns using saved encoders
    for col, encoder in encoders.items():
        if col in customer_data:
            customer_data[col] = encoder.transform([customer_data[col]])[0]

    # Create DataFrame in the exact feature order used during training
    input_data = pd.DataFrame([customer_data], columns=feature_columns)

    # Make prediction
    prediction = model.predict(input_data)[0]

    print("Prediction:", prediction)
    print("Probabilities:", model.predict_proba(input_data)[0])

    # Get probability
    probability = model.predict_proba(input_data)[0][1] * 100

    if prediction == "Yes":
        result = "Customer is likely to CHURN"
    else:
        result = "Customer is likely to STAY"

    return render_template(
        "index.html",
        prediction=result,
        probability=round(probability, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)