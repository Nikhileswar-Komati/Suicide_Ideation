from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from get_tweets import get_related_tweets


pipeline = load("suicide.joblib")


def requestResults(name):
    li = list()
    li.append(name)
    return pipeline.predict(li)
    

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name = user))


@app.route('/success/<name>')
def success(name):
    val = requestResults(name)
    if val == 0:
        text = 'Suicide'
    elif val == 1:
        text = 'Depression'
    else:
        text = 'Normal-Conversation'
    return "<center><h2> The entered text <i>" + name +"</i> is related to " + text + " </h2></center>"


if __name__ == '__main__' :
    app.run(debug=True)
