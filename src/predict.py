import mlflow.sklearn

def load_model(model_name):
    model = mlflow.sklearn.load_model(f"models:/{model_name}")
    return model

def predict(model, X):
    return model.predict(X)
