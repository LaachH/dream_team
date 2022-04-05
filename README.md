# **Group 3 - Group Assignment by Dream Team**
### Team : Peter Collins Gunin Khanna Lachlan Hume Jim Penner 

## **Background** 


### Building a Twitter dashboard that displays Sentiment and determines strength of correlation between Positive and/or Negative sentiment and Asset Prices and Volume & Volatility. Although twitter has only been around since 2006 there has already been instances where both here and overseas some financial influencers, either due to their role in particular companies or the size of their following on twitter have played a part in impacting shares and other assets.  We believe that we can show some correlations vs   


## Asset Selection 
### *Shares*:  For this exercise we have chosen 4 Australian shares:  Crown Casino, Dominos Pizza, Harvey Norman, and Premier Investments, all of which have featured in the news of late due to some controversial words, and or actions of their CEO's including recently the decision by the W.A government to ban Crown from operating a gaming license due to some potentially criminal behaviour and links.  Harvey Norman's CEO Gerry Harvey has often caused a furore on twitter so much so that in the past 6 months Harvey Norman has shut down it's Twitter account.  Much of the recent issues with Harvey Norman was their reluctance to pay back the JobKeeper payments despite the massive profits they gained due to the COVID Lockdown.  **Jim to add references here** 
### *Commodities* : Chosen are Corn, Wheat, Oil and the VIX or volatility index.  Oil is of most relevant now due to rising prices and the fact that even locally the federal government needed to step in and reduce the excise tax to bring about an immediate reduction in fuel prices. 
### *Meme stocks*: The meme stocks chosen are Tesla, Gamestop, AMC Entertainment and Blackberry;  
### *Bitcoin*:  The bitcoin assets selected are Bitcoin, Ethereum, Dogecoin, and Cardano  
## Methodology - Peter section 
### With sensitivity analysis, append to the list and get a print out of time, tweet, probability and sentiment.  Probability is indicating essentially the strength of Positive, or Negative (Neutral) tweet and then outputs either Positive or Negative as the resulting sentiment. 
### This is from Flair, which is a proven method for predicting share price movement based on sentiment. Then we sort the categories into positive and negative. Basic graph showing positive and negative tweets. 
### We have also looked at text blob which seems to have massive swings between positive and negative sentiment, which not much balance in the results. 
### **note that some of this will represent details and instructions on the coding itself** : ## called Elon's twitter id into the function get user tweets, and max is 100 and then built loop over it in order to get more tweets. Created a list with start date/end date and loops through everything you call into the data. Also cleans the tweet data.  From there create sentiment analysis.  This information is then appended to the list.  Create data frame and assign a variable to each list.    This creates a dataframe.  A list for tweets and one for dates.  
### use of counts to count tweets that have a word in it for example, or whatever you are querying.  Query was Tesla or Tsla so it produces tweets that have either of those words in it.    ### build a positive query where you select you do want to search on and then eliminate ones you don't ### created lists of tweets by date and probability and sentiment using Flair 
### set Elon Musk's twitter id & importing tweepy requires you to input secret API code once and then you can call it when needed 
## Methodology - Gunin section 
### Sensitivity analysis via Text blob and NLTK, in addition the data scraping provided emoji data as well.  We will look at utilising both Flair and NLTK.  Flair returns a sentiment string of either Positive or Negative, while NLTK gives a polarity score.  ### Do we concatenate that data together? 
