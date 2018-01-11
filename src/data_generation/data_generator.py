
#generates 7 files for each major party that contain N number of tweets for the corresonding party

import os
from tweet import Tweet
import csv
import shutil


#the major 7 german parties names as writeen in the train.csv, and a counter for the loaded tweets
parties_tweets_num = {"spd" : 0, "gruene" : 0, "cdu" : 0, "csu" : 0, "die-linke" : 0 , "afb" : 0, "fdp" : 0}
parties_tweets = {"spd" : [], "gruene" : [], "cdu" : [], "csu" : [], "die-linke" : [] , "afb" : [], "fdp" : []} 

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
        if  parties_tweets_num.has_key(party_name) and (parties_tweets_num[party_name] < max_tweets_number or max_tweets_number == -1):
            current_tweet = Tweet(row['tweet'])
            #preprocess the tweet, and get list of tokens
            tweet_tokens = current_tweet.getTokens()
            if len(tweet_tokens) > 0:
                output_tweet = ' '.join(tweet_tokens)
                parties_tweets[party_name].append(output_tweet)
                parties_tweets_num[party_name] +=1     
                 

#get min party tweets num
min_party_tweets = max_tweets_number+1 

if max_tweets_number != -1:
    for key in parties_tweets_num.keys():
        if parties_tweets_num[key] < min_party_tweets:
            min_party_tweets = parties_tweets_num[key]
# if we want to get all tweets
else:
    min_party_tweets = -1
#output tweets to parties files
for key in parties_tweets.keys():
    #output tweet to party file
    with open("out/" + key + '.txt', 'a') as party_file:
        for line in parties_tweets[key][0:min_party_tweets]:
            party_file.write(line+'\n')   

print("files were generated inside out folder")                    