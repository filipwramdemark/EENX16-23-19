from flask import Flask, render_template, request, redirect, url_for
import algoritm.NN.NN_predict as NN
import pandas as pd

snow_to_label_df = pd.read_csv('algoritm/snow_to_label.csv', names=['Snow', 'Label'])

snow_types_df = snow_to_label_df['Snow']

snow_to_label = snow_to_label_df.to_dict(orient='list') 


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', snow_types={0 : 'Konstsnö', 1 : 'Nysnö', 2 : 'Blandad snö', 3 : 'Skitig snö'})


# @app.route('/temp', methods=['GET'])
# def temp():
#     return render_template('temp.html')


# @app.route('/temp', methods=['POST'])
# def temp_post():
#     print("Temp:", request.form)
#     # T = float(request.form['text'])
#     # snow_ind = snow_to_label['Snow'].index(snow)
#     # snow_label = snow_to_label['Snow'][snow_ind]
#     # wax_label = predict([snow_label, T])
#     return render_template('label.html', label="hej")

@app.route('/snowtypes/<snow_type>', methods=["GET", "POST"])
def snow_types(snow_type : int):
    if request.method == "GET":
        return render_template('temp.html', snow_type=snow_type)
    elif request.method == "POST":
        T = float(request.form['temp'])

        wax = NN.predict([int(snow_type), T])

        return render_template('label.html', label=wax[0])
    else:
        return 404


if __name__ == "__main__":
    app.run()

