from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .data_preprocessing import load_and_process_data
from .predict import load_model, predict

app = FastAPI()

class PredictionRequest(BaseModel):
    data: dict

@app.post("/predict/rating")
def predict_rating(request: PredictionRequest):
    X, _, _ = load_and_process_data('data/raw/123.csv')  # Assuming we're using the same preprocessing
    model = load_model("LinearRegression_rating_Model")

    input_data = X.iloc[[0]]  # This should match the expected format, here we use a placeholder
    prediction = predict(model, input_data)

    return {"predicted_rating": prediction[0]}

@app.post("/predict/installs")
def predict_installs(request: PredictionRequest):
    X, _, _ = load_and_process_data('data/raw/123.csv')
    model = load_model("LinearRegression_number_of_installs_Model")

    input_data = X.iloc[[0]]  # This should match the expected format, here we use a placeholder
    prediction = predict(model, input_data)

    return {"predicted_installs": prediction[0]}
