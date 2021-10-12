from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from get_tweets import get_related_tweets


pipeline = load("suicide.joblib")
def transform(value):
    if value == 0:
        return 'Suicide'
    elif value == 1:
        return 'Depression'
    return 'Normal_Conversation'


def requestResults(name):
    tweets = get_related_tweets(name)
    tweets['prediction'] = pipeline.predict(tweets['tweet'])
    tweets['prediction'] = tweets['prediction'].apply(lambda x: transform(x))
    data = '\n' + str(tweets.prediction.value_counts()) + '\n\n'
    return "The entered Keyword is " + name + data + str(tweets)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('suicide.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(requestResults(name)) + " </xmp> "


if __name__ == '__main__' :
    app.run(debug=True)
