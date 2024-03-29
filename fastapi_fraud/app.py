import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route('/')
def index():
    return {'message': '기계학습 API - 위조지폐 인식'}

@app.route('/predict', methods=['POST'])
def predict_banknote(data:BankNote):
    data = data.dict()
    variance = data['variance']
    skweness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    
    prediction = classifier.predict([[variance, skweness, curtosis, entropy]])
    
    if(prediction[0] > 0.5):
        prediction="Fake"
    else:
        prediction="Real"
        
    return {
        'prediction': prediction
    }
    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1", port=8000')