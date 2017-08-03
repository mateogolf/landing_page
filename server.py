from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def openindex():
    return render_template('index.html')
@app.route('/ninjas')
def Ninja():
    return render_template('ninjas.html')


@app.route('/dojo/news')
def dojo():
    return render_template('dojo.html')


app.run(debug=True)
