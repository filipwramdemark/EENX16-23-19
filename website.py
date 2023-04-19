from flask import Flask, render_template, request, redirect, url_for
import algoritm.NN.NN_predict as NN
import algoritm.DecisionTree.Tree_Predict as tree
import algoritm.SVM.SVM_predict as SVM
import pandas as pd


snow_to_label_df = pd.read_csv("algoritm/snow_to_label.csv", names=["Snow", "Label"])

snow_types_df = snow_to_label_df["Snow"]

snow_to_label = snow_to_label_df.to_dict(orient="list") 

snow = {snow_to_label["Label"][i] : snow_to_label["Snow"][i] for i in range(len(snow_to_label["Snow"]))}

waxes = pd.read_csv("algoritm/label_to_wax.csv").iloc[:,1].to_list()

print(waxes)

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

        input = [int(snow_type), T]

        wax_NN = NN.predict(input)
        wax_tree = tree.Treepredict(input)
        wax_SVM = SVM.predict(input)

        return render_template("label.html", snow_type=snow_type, label_NN1=wax_NN[0], label_NN2=wax_NN[1], label_NN3=wax_NN[2], label_tree=wax_tree, 
                               label_SVM1=wax_SVM[0], label_SVM2=wax_SVM[1], label_SVM3=wax_SVM[2])
    else:
        return 404


@app.route("/snowtypes/<snow_type>/feedback", methods=["GET", "POST"])
def feedback(snow_type : int):
    # return (snow)
    return render_template("feedback.html", snow_type=snow_type)


@app.route("/snowtypes/<snow_type>/wax", methods=["GET", "POST"])
def wax(snow_type : int):
    if request.method == "GET":
        return render_template("wax.jinga2", snow_type=snow_type, waxes=waxes)
    elif request.method == "POST":
        wax = request.form["wax"]
        return render_template("done.html")

@app.route("/done")
def done():
    return render_template("done.html")

if __name__ == "__main__":
    app.run()