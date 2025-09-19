import joblib
import os
import numpy as np

# Load model at startup
def model_fn(model_dir):
    model_path = os.path.join(model_dir, "model.joblib")
    return joblib.load(model_path)

# Input: CSV string
def input_fn(request_body, content_type="text/csv"):
    if content_type == "text/csv":
        data = np.array([x.split(",") for x in request_body.splitlines()]).astype(float)
        return data
    else:
        raise ValueError(f"Unsupported content type: {content_type}")

# Prediction
def predict_fn(input_data, model):
    return model.predict_proba(input_data)[:, 1]

# Output: JSON
def output_fn(prediction, accept="application/json"):
    return {"churn_probability": prediction.tolist()}

