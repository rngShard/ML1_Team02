
import os 
import gensim
from tweet import Tweet
from word_vectorizer import WordVectorizer
import csv


#load the word2vec module
#word2vecModule = gensim.models.KeyedVectors.load_word2vec_format('./embed_tweets_de_200M_200D/embedding_fil
word2vecModule = []

#initialize thw WordVectorizer model
word_vectorizer = WordVectorizer(word2vecModule)

# load train data file to get the tweets
with open('../tweetsCrawler/train.csv','r') as train_data:
    #write tweets and its matrix to vectors.csv
    with open('./vectors.csv', 'w') as vectors_data:

        writer = csv.writer(vectors_data)
        #write headr row to vectors.csv
        writer.writerow(["politician_name", "party","tweet","matrix"])
        #rows to be written to vectors.csv
        out_rows = []
        
        reader = csv.DictReader(train_data)
        for row in reader:
            current_tweet = Tweet(row['tweet'])
            #preprocess the tweet, and get list of tokens 
            current_tweet_tokens = current_tweet.getTokens()
            # get the corresponding matrix for the current_tweet
            tweet_matrix,percentageOfMissingWords = word_vectorizer.getMatrix(current_tweet_tokens)
            out_rows.append([row["politician_name"], row["party"], row["tweet"], tweet_matrix])

        #write output rows to vectors.csv
        writer.writerows(out_rows)


