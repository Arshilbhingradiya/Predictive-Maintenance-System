from flask import Flask, render_template, request
import pickle
import numpy as np
import pyttsx3 as pt

app = Flask(__name__)


model = pickle.load(open('app/models/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  
    air_temp = float(request.form['air_temp'])
    process_temp = float(request.form['process_temp'])
    rotational_speed = float(request.form['rotational_speed'])
    torque = float(request.form['torque'])
    tool_wear = float(request.form['tool_wear'])

   
    input_data = np.array([[air_temp, process_temp, rotational_speed, torque, tool_wear]])

    prediction = model.predict(input_data)


    if prediction[0] == 1:
        return render_template('index.html', prediction_text='Maintenance Required', alert=True)
    else:
        return render_template('index.html', prediction_text='No Maintenance Needed', alert=False)

if __name__ == '__main__':
    app.run(debug=True)
