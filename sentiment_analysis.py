import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(quote):
  """
  Analyzes the sentiment of a given quote using the VADER sentiment analyzer.

  Args:
    quote: The quote to analyze.

  Returns:
    A string representing the sentiment: "positive", "negative", or "neutral".
  """
  nltk.download('vader_lexicon') 
  sia = SentimentIntensityAnalyzer()
  sentiment_score = sia.polarity_scores(quote)['compound']

  if sentiment_score > 0.05:
    return "positive"
  elif sentiment_score < -0.05:
    return "negative"
  else:
    return "neutral"