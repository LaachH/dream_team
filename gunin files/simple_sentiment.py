#from tokenize import String
from textblob import TextBlob as tb
import pandas as pd
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer as Sia
from gensim.parsing.preprocessing import remove_stopwords
from pathlib import Path
import seaborn as sns
from googletrans import Translator

#%matplotlib inline

nltk.download('vader_lexicon')

sia = Sia()
emoji_raw = pd.read_html("https://kt.ijs.si/data/Emoji_sentiment_ranking")
emoji_lookup_df = emoji_raw[0][['Char', 'Sentiment score[-1...+1]']]
emoji_lookup_df.rename(columns={'Sentiment score[-1...+1]': 'sentiment_score'}, inplace = True)


def clean_text(input_str: str) -> str:
    input_str = input_str.lower()
    input_str = re.sub("[^A-Za-z0-9]"," ",input_str)
    input_str = re.sub(r'^https?:\/\/.*[\r\n]*', '', input_str, flags=re.MULTILINE)
    input_str = re.sub(r"www.\S+",'',input_str)
    input_str = remove_stopwords(input_str)
    return input_str

def get_tb_score(text: str) -> float:
    return tb(text).sentiment[0]

def get_nltk_score(text: str) -> float:
    return sia.polarity_scores(text)['compound']

def build_sentiment_df(tweet_dataframe, target_column, incl_clean_text, incl_emoji_data, ignore_non_eng):
    # getting the corresponding data in lists
    raw_tweets = tweet_dataframe[target_column].tolist()
    cleaned_tweets = [clean_text(i) for i in raw_tweets]
    tb_polarity = [tb(i).sentiment[0] for i in cleaned_tweets]
    nltk_polarity = [sia.polarity_scores(i)['compound'] for i in cleaned_tweets]
    
    # building the dataframe
    final_df = pd.DataFrame()
    final_df['tweets'] = raw_tweets
    final_df['textblob_polarity'] = tb_polarity
    final_df['nltk_polarity'] = nltk_polarity

    if incl_clean_text == True:
        final_df['cleaned_tweets'] = cleaned_tweets
        final_df = final_df[['tweets', 'cleaned_tweets', 'textblob_polarity', 'nltk_polarity']]
    if incl_emoji_data == True:
        # add function for emoji lookup
        return final_df
    if ignore_non_eng == True:
        # add function for non english tweets
        return final_df

    return final_df['nltk_polarity'][0]
              

