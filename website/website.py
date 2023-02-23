from flask import Flask, render_template, request


def cal(x):
    return x + 1

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Konstsnö':
            x = cal(3)
            return ("Swix V40")
        elif  request.form.get('action2') == 'Nysnö':
            x = cal(5)
            return ("Swix KX75")
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

# @app.route("/test/")
# def test():
#     return "Hello! this is the main page <h1>HELLO</h1>"

if __name__ == "__main__":
    app.run()

