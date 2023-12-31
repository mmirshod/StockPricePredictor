import joblib
import numpy as np

def preprocess(Open: float, High: float, Low: float, Volume: int):
    test_data = np.array([[Open, High, Low, Volume]])
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test_data)

    return prediction
