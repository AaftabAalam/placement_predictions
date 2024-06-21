from flask import Flask,render_template,request
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    cgpa = float(request.form.get('cgpa'))
    iq = int(request.form.get('iq'))
    profile_score = int(request.form.get('profile_score'))

    #prediction

    input_data = np.array([cgpa,iq,profile_score]).reshape(1,-1)
    scaled_input = scaler.transform(input_data)
    result = model.predict(scaled_input)

    if result[0] == 1:
        result = 'Congratulation, this student will be placed'
    else:
        result = 'Regretfully this student will not be placed'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(debug=True)