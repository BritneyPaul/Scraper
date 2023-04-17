# from stanfordcorenlp import StanfordCoreNLP
# import numpy as np
# piodbc
# pandas
# nltk
# nltk.download('vader_lexicon')
# nltk.sentiment.vader import SentimentIntesitAnalyzer


# import pandas as pd
# import nltk
# from textblob import TextBlob

# # Load CSV file into Pandas DataFrame
# df = pd.read_csv("C:/Usersbpaul/OneDrive/Desktop/DEDSW8/reviews/Bol_reviews.csv")

# # Define a function to tokenize the reviews using NLTK
# def tokenize(text):
#     tokens = nltk.word_tokenize(text)
#     return tokens

# # Tokenize the reviews and store them in a new column
# df['tokens'] = df['review'].apply(tokenize)

# # Define a function to get the sentiment score using TextBlob
# def get_sentiment(text):
#     sentiment = TextBlob(text).sentiment.polarity
#     return sentiment

# # Get the sentiment score for each review and store it in a new column
# df['sentiment'] = df['review'].apply(get_sentiment)

# # Print the DataFrame with the sentiment scores
# print(df)


import pandas as pd
from textblob import TextBlob
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')

# Load CSV file into Pandas DataFrame
df = pd.read_csv('C:/Usersbpaul/OneDrive/Desktop/DEDSW8/reviews/Bol_reviews.csv')

# Define function to clean text and tokenize it
from nltk.corpus import stopwords
stopwords = stopwords.words('dutch')

def tokenize(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stopwords]
    return tokens

# Tokenize the reviews and store the tokenized text in a new column
df['tokenized_text'] = df['review'].apply(tokenize)

# Define function to get sentiment score
def get_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    return sentiment

# Get the sentiment score for each review and store it in a new column
df['sentiment_score'] = df['review'].apply(get_sentiment)

# Print the DataFrame with the sentiment scores
print(df)
