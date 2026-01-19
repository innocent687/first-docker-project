# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from model import predict

app = FastAPI()

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "ML model is running!"}

@app.post("/predict")
def get_prediction(data: IrisFeatures):
    features = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]
    result = predict(features)
    return {"prediction": result}