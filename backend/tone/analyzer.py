import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def detect_tone(message):
    score = sia.polarity_scores(message)
    if score["compound"] > 0.5:
        return "positive"
    elif score["compound"] < -0.5:
        return "negative"
    return "neutral"
