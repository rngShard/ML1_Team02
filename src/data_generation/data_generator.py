
#generates 7 files for each major party that contain N number of tweets for the corresonding party

import os
from tweet import Tweet
import csv
import shutil


#the major 7 german parties names as writeen in the train.csv, and a counter for the loaded tweets
major_parties = {"spd" : 0, "gruene" : 0, "cdu" : 0, "csu" : 0, "die-linke" : 0 , "afb" : 0, "fdp" : 0}

#delete output folder if exist
if os.path.exists("out"):
    shutil.rmtree("out")

#create out folder
os.makedirs("out")

# load train data file to get the tweets
with open('../tweetsCrawler/train.csv','r') as train_data:

    max_tweets_number = int(raw_input("enter max number of tweets for each party or -1 to get all tweets"))

    reader = csv.DictReader(train_data)
    for row in reader:
        party_name = row['party']
        #check if the current tweet's party is major one, and if we still need tweets for this party
        if  major_parties.has_key(party_name) and (major_parties[party_name] < max_tweets_number or max_tweets_number == -1):
            current_tweet = Tweet(row['tweet'])
            #preprocess the tweet, and get list of tokens
            tweet_tokens = current_tweet.getTokens()
            if len(tweet_tokens) > 0:
                output_tweet = ' '.join(tweet_tokens)
                #output tweet to party file
                with open("out/" + party_name + '.txt', 'a') as party_file:
                    party_file.write(output_tweet +'\n')
                    major_parties[party_name] +=1 

print("files were generated inside out folder")                    