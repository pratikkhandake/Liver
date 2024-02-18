# app.py

from flask import Flask, request, render_template
import pickle
from config import port_number

app = Flask(__name__)

# Load the pre-trained model
with open('liver.pkl', 'rb') as f:
    model = pickle.load(f)

# Define homepage API
@app.route('/')
def home():
    return render_template('index.html')

# Define prediction API
@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from the request
    age = float(request.form['Age'])
    tb = float(request.form['TB'])
    db = float(request.form['DB'])
    gender = request.form['Gender']
    alkphos = float(request.form['Alkphos'])
    sgpt = float(request.form['Sgpt'])
    sgot = float(request.form['Sgot'])
    tp = float(request.form['TP'])
    alb = float(request.form['ALB'])
    ag_ratio = float(request.form['A_G_Ratio'])

    # Convert 'Gender' to numerical format
    gender = 1 if gender == 'Male' else 0
    
    # Make prediction
    prediction = model.predict([[age, tb, db, gender, alkphos, sgpt, sgot, tp, alb, ag_ratio]])
    if prediction[0] == 1:
        result = 'Liver Disease Detected'
    else:
        result = 'No Liver Disease Detected'

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(port=port_number, debug=False)
