import pandas as pd
import pyodbc
from sqlalchemy import create_engine
import csv
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import nltk
import os
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Define the connection details for the SQL Server database
server_name = 'BRITNEY'
database_name = 'reviewAnalysis'
driver = '{ODBC Driver 17 for SQL Server}'

# Create a SQLAlchemy engine object
engine = create_engine(f"mssql+pyodbc://{server_name}/{database_name}?driver={driver}")

# Create a pyodbc connection object
conn = pyodbc.connect(f"DRIVER={driver};SERVER={server_name};DATABASE={database_name};Trusted_Connection=yes")


# Define function to clean text and tokenize it
from nltk.corpus import stopwords
stopwords = stopwords.words('dutch')

def tokenize(text):
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stopwords]
    return tokens

# Define function to get sentiment label using NLTK's Vader
sia = SentimentIntensityAnalyzer()

def get_sentiment_label(text):
    sentiment = sia.polarity_scores(text)['compound']
    if sentiment > 0.05:
        return 'positive'
    elif sentiment < -0.05:
        return 'negative'
    else:
        return 'neutral'

# Loop through all the files in the review folder
folder_path = 'C:/Users/bpaul/OneDrive/Desktop/DEDSW8/reviews/'
all_tokens = []
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        # Load CSV file into Pandas DataFrame
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        
        # Tokenize the reviews and store the tokenized text in a new column
        df['tokenized_text'] = df['reviews'].apply(tokenize)
        all_tokens.extend([token for review_tokens in df['tokenized_text'] for token in review_tokens])

        
        # Get the sentiment label for each review and store it in a new column
        df['sentiment_label'] = df['reviews'].apply(get_sentiment_label)
        

        # Insert the results into the SQL Server table      
        cursor = conn.cursor()
        for index, row in df.iterrows():
            review = row['reviews']
            sentiment = row['sentiment_label']
            query = "INSERT INTO dbo.Analysis (review, sentiment) VALUES (?, ?)"
            cursor.execute(query, review, sentiment)
            conn.commit()
       

        # Print a message to indicate that the results have been inserted into the database
        print(f"Sentiment analysis results for file '{file_name}' have been inserted into the database.")
        print()

# Create a frequency distribution of the words
freq_dist = FreqDist(all_tokens)

# Print the 10 most common words
print("10 most common words:")
print(freq_dist.most_common(10)) 


# Get the 10 most frequent words
most_common_words = Counter(all_tokens).most_common(10)

# Open a file for writing
with open('most_frequent_words.csv', 'w', newline='') as f:
    # Create a CSV writer object
    writer = csv.writer(f)
    # Write the header row
    writer.writerow(['Word', 'Frequency'])
    # Write each word and its frequency to the CSV file
    for word, count in most_common_words:
        writer.writerow([word, count])























        # print t terminal
        # # Print the DataFrame with the sentiment labels
        # print(f"Sentiment analysis results for file '{file_name}':")
        # print(df[['reviews', 'sentiment_label']])
        # print()

















# import pandas as pd

# # Load CSV file into Pandas DataFrame
# df = pd.read_csv('C:/Users/bpaul/OneDrive/Desktop/DEDSW8/reviews/Bol_reviews.csv')

# # Drop rows containing missing values
# df.dropna(inplace=True)

# # Print the cleaned DataFrame
# print(df)
