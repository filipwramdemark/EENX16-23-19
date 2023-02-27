from flask import Flask, render_template, request, redirect, url_for
import algoritm.NN.NN_predict as NN
import pandas as pd

snow_to_label_df = pd.read_csv("algoritm/snow_to_label.csv", names=["Snow", "Label"])

snow_types_df = snow_to_label_df["Snow"]

snow_to_label = snow_to_label_df.to_dict(orient="list") 

snow = {snow_to_label["Label"][i] : snow_to_label["Snow"][i] for i in range(len(snow_to_label["Snow"]))}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", snow_types=snow)


@app.route("/snowtypes/<snow_type>", methods=["GET", "POST"])
def snow_types(snow_type : int):
    if request.method == "GET":
        return render_template("temp.html", snow_type=snow_type)
    elif request.method == "POST":
        T = float(request.form["temp"])

        wax = NN.predict([int(snow_type), T])

        return render_template("label.html", label1=wax[0], label2=wax[1], label3=wax[2])
    else:
        return 404


if __name__ == "__main__":
    app.run()

