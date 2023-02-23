from flask import Flask, render_template, request, redirect, url_for

snow = ''

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
    T = request.form['text']
    return T

if __name__ == "__main__":
    app.run()


