import pickle

import joblib
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocessing import preprocess_data

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'m': 'Welcome to the Purchase Prediction API'})


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)
    processed_data = preprocess_data(data)
    input_array = processed_data.values
    # Load mô hình đã huấn luyện từ file
    with open('knn_model.joblib', 'rb') as model_file:
        knn = joblib.load(model_file)
    prediction = knn.predict(input_array)
    print('result:', prediction[0])

    return jsonify({'prediction': bool(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
