
# Diabetes Prediction API using Flask

This is a simple Flask API that uses a Machine Learning model to predict whether a person is diabetic or not based on health metrics.

##  Tech Stack

- Python
- Flask
- scikit-learn
- Pandas
- Postman (for testing)

##  Model Info

- Model: Logistic Regression
- Trained on: PIMA Diabetes Dataset (`diabetes.csv`)
- Preprocessing: StandardScaler

##  Project Structure

```

Flask\_ML\_API/
├── model/
│   ├── scaler.pkl
│   └── model.pkl
├── main.py
├── requirements.txt
├── diabetes.csv       # (optional for context)
└── README.md

````

##  How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/Flask-ML-Diabetes-API.git
cd Flask-ML-Diabetes-API
````

### 2. Set up virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python main.py
```

The app will be running at: `http://127.0.0.1:5000`

---

##  API Endpoint

### `POST /predict`

**URL:** `http://127.0.0.1:5000/predict`
**Method:** `POST`
**Content-Type:** `application/json`

#### Sample Request (Use in Postman or curl)

```json
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}
```

####  Sample Response

```json
{
  "prediction": "Diabetic"
}
```

---

##  Error Handling

The API returns clear error messages for various common issues:

###  Missing Input

If no data is provided:

```json
{
  "error": "Input data is not Provided"
}
```

Status code: `400 Bad Request`

---

###  Missing Required Fields

If required fields are missing from the input:

```json
{
  "error": "Required columns missing. Required columns : ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']"
}
```

Status code: `400 Bad Request`

---

###  Internal Server Errors

Any unexpected exceptions are caught and returned like this:

```json
{
  "error": "Some error message from the server"
}
```

Status code: `500 Internal Server Error`

---

##  Required Input Fields

Make sure your JSON contains **all** of these fields:

* `Pregnancies`
* `Glucose`
* `BloodPressure`
* `SkinThickness`
* `Insulin`
* `BMI`
* `DiabetesPedigreeFunction`
* `Age`

---

##  Note

This project is meant for educational and portfolio purposes. The model was trained on a public dataset and the API is intended for demo/testing use.

---
## Postman Screenshot
<img width="1440" alt="Screenshot 2025-06-05 at 1 35 27 AM" src="https://github.com/user-attachments/assets/4bff2010-241b-49bb-aa2c-aa2409de3d1d" />

---

## Author

**Naveen Kumar Roy**


---

