from flask import Flask, request, jsonify
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

loaded_model = joblib.load('rf_model.pkl')
df_s = pd.read_csv('./Symptom-severity.csv')
df_s['Symptom'] = df_s['Symptom'].str.replace('_', ' ')

@app.route('/predict', methods=['GET'])
def predict():
    try:
        symptoms = request.args.get('symptoms')
        symptoms = symptoms.split(',') if symptoms else []

        prediction = make_prediction(symptoms)

        response = {'prediction': prediction}
        return jsonify(response), 200 
    except Exception as e:
        return jsonify({'error': str(e)}), 400  

def make_prediction(symptoms):
    x = np.array(df_s['Symptom'])
    y = np.array(df_s['weight'])
    for i in range(len(symptoms)):
        for j in range(len(x)):
            if symptoms[i] == x[j]:
                symptoms[i] = y[j]
    input_data = [symptoms]
    pred = loaded_model.predict(input_data)
    return pred[0]

if __name__ == '__main__':
    app.run(debug=True)
