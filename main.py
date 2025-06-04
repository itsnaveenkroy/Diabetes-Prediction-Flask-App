import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load scaler
with open('model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Load model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return "Diabetes Prediction App is running"

@app.route("/predict", methods=["POST"]) #endpoint
def predict():
    try:
        # get the JSON data from the api request
        data = request.get_json()

        input_data = pd.DataFrame([data])

        # check if input is provided
        if not data:
            return jsonify({"error":"Input data is not Provided"}), 400


        # Validate input columns
        required_columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
         "BMI", "DiabetesPedigreeFunction", "Age"]

        if not all(col in input_data.columns for col in required_columns):
            return jsonify({"error": f"Required columns missing. Required columns : {required_columns}"}), 400
        
        #scale the data
        scaled_data = scaler.transform(input_data)

        #make prediction
        prediction = model.predict(scaled_data)


        #response
        response = {
            "prediction": "Diabetic" if prediction[0]==1 else "Non Diabetic"
        }
        return jsonify(response)

    #internal server error
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__=="__main__":
    app.run(debug=True)
