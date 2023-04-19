# Twitter Sentiment Prediction

This is a data engineering project that predicts the sentiment of the most recent tweets for a given prompt using VADAR and snscrape. The app's stack is Python, Flask, Bootstrap, and Azure.

## Application

The application is hosted on azure at https://twitter-prediction-sentiment.azurewebsites.net/

## Requirements

To run the app locally, you need to have the following installed:

- Python 3.7 or higher
- Flask 2.0.1 or higher

## Installation

To install and run the app locally, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/twitter-sentiment-prediction.git`
2. Create a virtual environment and activate it: `python -m venv venv` and `source venv/bin/activate`
3. Install the dependencies: `pip install -r requirements.txt`
4. Set up the environment variables by creating a `.env` file in the root directory with the following content:

FLASK_APP=app.py
FLASK_ENV=development


5. Start the app: `flask run`

## Usage

Once the app is running, you can access it at `http://localhost:5000`. Enter a prompt (e.g., "COVID-19 vaccine") and click the "Predict" button. The app will fetch the most recent tweets related to the prompt using snscrape, analyze their sentiment using VADAR, and display the results in a table with the tweet text, sentiment score, and sentiment label (positive, neutral, or negative).

## Credits

This project was created by [Your Name](https://github.com/ajoeviola). The app uses the [VADAR](https://github.com/cjhutto/vaderSentiment) library for sentiment analysis, [snscrape](https://github.com/JustAnotherArchivist/snscrape) for fetching tweets, and has an [html5](https://html5up.net/) template
