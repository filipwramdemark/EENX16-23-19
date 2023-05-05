from flask import Flask, render_template, request, redirect, url_for
import algoritm.NN.NN_predict as NN
import algoritm.DecisionTree.Tree_Predict as tree
import algoritm.SVM.SVM_predict as SVM
import algoritm.NN.NN as NN_model
import algoritm.SVM.SVM as SVM_model
import algoritm.DecisionTree.Decisiontree as tree_model
import pandas as pd
import matinstrumentClientSide
import accelorometer
import dataAnalys
import Feedback


snow_to_label_df = pd.read_csv("algoritm/snow_to_label.csv", names=["Snow", "Label"])
snow_types_df = snow_to_label_df["Snow"]
snow_to_label = snow_to_label_df.to_dict(orient="list") 
snow = {snow_to_label["Label"][i] : snow_to_label["Snow"][i] for i in range(len(snow_to_label["Snow"]))}

waxes = pd.read_csv("algoritm/label_to_wax.csv", header=None).iloc[:,1].to_list()
labels = pd.read_csv("algoritm/label_to_wax.csv", header=None).iloc[:,0].to_list()
wax_to_label = {waxes[i] : labels[i] for i in range(len(waxes))}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", snow_types=snow)


@app.route("/snowtypes/<snow_type>", methods=["GET", "POST"])
def snow_types(snow_type : int):
    return render_template("wait.html", snow_type=snow_type)

 
@app.route("/snowtypes/<snow_type>/temp", methods=["GET", "POST"])
def temp(snow_type : int):
    if request.method == "GET":
        return render_template("temp.html", snow_type=snow_type)
    elif request.method == "POST":
        T = float(request.form["temp"])

        input = [int(snow_type), T, 0, 0, 0]

        wax_NN = NN.predict(input)
        wax_tree = tree.Treepredict(input)
        wax_SVM = SVM.predict(input)

        return render_template("label.html", snow_type=snow_type, label_NN1=wax_NN[0], label_NN2=wax_NN[1], label_NN3=wax_NN[2], label_tree=wax_tree, 
                               label_SVM1=wax_SVM[0], label_SVM2=wax_SVM[1], label_SVM3=wax_SVM[2])
    else:
        return 404



@app.route("/snowtypes/<snow_type>/feedback", methods=["GET", "POST"])
def feedback(snow_type : int):
    if request.method == "GET":
        return render_template("wax.jinga2", snow_type=snow_type, waxes=waxes)
    elif request.method == "POST":
        wax = request.form["wax"]
        wax = wax_to_label[wax]

        return render_template("eval.html", snow_type=snow_type, wax=wax)
    else:
        return 404


# @app.route("/snowtypes/<snow_type>/wax", methods=["GET", "POST"])
# def wax(snow_type : int):
#     if request.method == "GET":
#         return render_template("wax.jinga2", snow_type=snow_type, waxes=waxes)
#     elif request.method == "POST":
#         wax = request.form["wax"]
#         return render_template("done.html")



# @app.route("/snowtypes/<snow_type>/input", methods=["GET", "POST"])
# def input(snow_type :int): 
#     return render_template("wait.html", snow_type=snow_type)



@app.route("/snowtypes/<snow_type>/input", methods=["GET", "POST"])
def wait(snow_type : int):

    matinstrumentClientSide.getData()
    temp_and_hum = pd.read_csv("tempAndHum.csv", header=None).values.tolist()

    for i in range(len(temp_and_hum)):
        temp_and_hum[i] = temp_and_hum[i][0]

    input = [int(snow_type)] + temp_and_hum


    wax_NN = NN.predict(input)
    wax_tree = tree.Treepredict(input)
    wax_SVM = SVM.predict(input)

    return render_template("label.html", snow_type=snow_type, label_NN1=wax_NN[0], label_NN2=wax_NN[1], label_NN3=wax_NN[2], label_tree=wax_tree, 
                            label_SVM1=wax_SVM[0], label_SVM2=wax_SVM[1], label_SVM3=wax_SVM[2])


@app.route("/snowtypes/<snow_type>/feedback/eval/<wax>", methods=["GET", "POST"])
def eval(snow_type : int, wax : int):

    # accelorometer.getAccData()
    
    if dataAnalys.testData():
        temp_and_hum = pd.read_csv("tempAndHum.csv", header=None).values.tolist()

        for i in range(len(temp_and_hum)):
            temp_and_hum[i] = temp_and_hum[i][0]

        input = [int(snow_type)] + [temp_and_hum[0]] + [int(wax)] + temp_and_hum[1:]

        # print(input)
        Feedback.savefeedback(input)

        NN_model.trainNN()
        SVM_model.trainSVM()
        tree_model.trainTree()

    return render_template("done.html")




@app.route("/done")
def done():
    return render_template("done.html")

if __name__ == "__main__":
    app.run()


