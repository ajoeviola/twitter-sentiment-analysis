from flask import Flask
from flask import Flask, redirect, render_template, request, url_for
from scrape import get_tweets
from sentiment_prediction import predict_sentiment
import json
import plotly
import plotly.express as px



app = Flask(__name__, static_folder="static")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template("index.html")


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        prompt = request.form["prompt"]
        tweets = request.form["NumberOfTweets"]

        #get sentiment analysis
        get_tweets(prompt, tweets)
        data = predict_sentiment()
        try:
            num_positive = int(data['classification'].value_counts()['positive'])
        except KeyError:
            num_positive = 0

        try:
            num_negative = int(data['classification'].value_counts()['negative'])
        except KeyError:
            num_negative = 0
        
        try:
            num_neutral = int(data['classification'].value_counts()['neutral'])
        except KeyError:
            num_neutral = 0



        fig = px.histogram(data, x='classification', color='classification', color_discrete_sequence=["red", "grey", "blue"])

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template("generic.html", prediction_text=f'Positive tweets: {num_positive} Negative tweets: {num_negative} Neutral tweets: {num_neutral}',graphJSON=graphJSON)
    return render_template("generic.html")

if __name__ == "__main__":
    app.run(debug=True)