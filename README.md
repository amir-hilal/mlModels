# Model Prediction Project

This project is designed to create and deploy models for predicting ratings and the number of installs using Linear Regression and Random Forest Regression. The models are containerized using Docker and deployed on AWS.

## Project Structure

- `data/`: Contains raw and processed data.
- `models/`: Contains trained models and MLflow artifacts.
- `notebooks/`: Contains Jupyter notebooks for EDA and feature engineering.
- `src/`: Contains source code including data preprocessing, model training, prediction scripts, and FastAPI app.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: Python dependencies.

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the FastAPI server: `uvicorn src.app:app --reload`.

## Docker Instructions

1. Build the Docker image: `docker build -t my_model_image .`
2. Run the Docker container: `docker run -p 8000:8000 my_model_image`

## Deployment on AWS

Instructions for deploying the Docker container on AWS are included in the project.
