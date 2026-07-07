from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="MLOps Prediction API")

# Load model once when the application starts
model = joblib.load("models/model.pkl")


class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/predict")
def predict(data: IrisRequest):

    prediction = model.predict([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    return {
        "prediction": int(prediction[0])
    }
