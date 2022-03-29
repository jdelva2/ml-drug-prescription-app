from flask import Flask

import pickle
from flask import request, jsonify,render_template,flash

app =Flask(__name__)

gender_map = {"F": 0, "M": 1}
bp_map = {"HIGH": 0, "LOW": 1, "NORMAL":2}
cholesterol_map = {"HIGH": 0, "NORMAL": 1}
drug_map = {0:"DRUG Y", 3: "DRUG C", 4: "DRUG X", 1:"DRUG A", 2: "DRUG  B"}

def predict_drug(Age,Sex,BP,Cholesterol,Na_to_K):
    #1 Read the machine learning model from its saved state
    pickle_file = open('model.pkl', 'rb')
    model = pickle.load(pickle_file)
    #2 Transform the "raw data" passed into the function to the encoded / numerical values using the maps / dictionaries
    Sex = gender_map[Sex]
    BP = bp_map[BP]
    Cholesterol = cholesterol_map[Cholesterol]
    
    #3 Make an individual prediction for this set of data
    y_predict = model.predict([[Age,Sex,BP,Cholesterol,Na_to_K]])[0]
    
    #4 Return the "raw" version of the prediction i.e the actual name of the drug rather than the numerical encoded version
    return drug_map[y_predict]

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/drug', methods = ['POST', 'GET'])
def prescribe():
    
    Age = int(request.form['age_input'])
    Sex = request.form['sex_input']
    BP = request.form['bp_input']
    Cholesterol = request.form['cholesterol_input']
    Na_to_K = float(request.form['na_to_k_input'])
    
    drug = predict_drug(Age,Sex,BP,Cholesterol,Na_to_K)
    
    return render_template('index.html', prediction_text='Recommended Drug: {}'.format(drug))

if __name__ == '__main__':
    app.run()