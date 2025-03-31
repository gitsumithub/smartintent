import joblib
import os

model_path = os.path.join("model", "classifier.pkl")
pipeline = joblib.load(model_path)

def predict_intent(text):
    return pipeline.predict([text])[0]
