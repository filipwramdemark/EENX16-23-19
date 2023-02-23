from flask import Flask, render_template, request, redirect, url_for
from algoritm.NN.NN_predict import predict
import pandas as pd

snow = ''

snow_to_label_df = pd.read_csv('algoritm/snow_to_label.csv', names=['Snow', 'Label'])
snow_to_label = snow_to_label_df.to_dict(orient='list')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Konstsnö':
            global snow
            snow = 'Konstsnö'
        elif  request.form.get('action2') == 'Nysnö':
            snow = 'Nysnö'
        return redirect(url_for('temp'))
        
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html')

@app.route('/temp')
def temp():
    return render_template('temp.html')


@app.route('/temp', methods=['POST'])
def temp_post():
    T = float(request.form['text'])
    snow_ind = snow_to_label['Snow'].index(snow)
    snow_label = snow_to_label['Snow'][snow_ind]
    wax_label = predict([snow_label, T])
    return wax_label[0]

if __name__ == "__main__":
    app.run()