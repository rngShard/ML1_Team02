import re
import os
import csv
import tweepy
import time
from tweet import Tweet

class TwitterFetcher:
    def __init__(self,user_name):
        self.user_name = user_name
        #twitter app access tokens
        __consumer_key = "TcoDRSehIlGkWfxM0uXADVVKN"
        __consumer_secret = "u343Uv4Ta54zoHp5PALoXd5fYpSVhSfynUqqAQVwsn3cMtriPD"
        __access_key = "939464114606346240-rdJ9A9I4XuW76R2ClHLuBDtiImRWT0h"
        __access_secret = "JDbzppXonkV52rbG2pJcx92p1L0BuR8Xaz8dh3nEsPK8f"
        #initialize the twitter API
        auth = tweepy.OAuthHandler(__consumer_key, __consumer_secret)
        auth.set_access_token(__access_key, __access_secret)
        self.__twitter_api = tweepy.API(auth)

    def do_task(self,max_tweets_num):
        user_tweets = self.__get_user_tweets(max_tweets_num)
        print("Number of tweets fetched by TFetcher:", len(user_tweets))
        with open("output/"+self.user_name + ".txt", "w") as f:
            for tweet in user_tweets:
                f.write(tweet + "\n")

    def __get_user_tweets(self, max_tweets_num):
        user_tweets = []

        try:
            first_tweets_num = 1
            if max_tweets_num%200 > 0:
                first_tweets_num = max_tweets_num % 200
            recent_tweets = self.__twitter_api.user_timeline(screen_name = self.user_name, count = first_tweets_num)
            for tweet in recent_tweets:
                currentTweet = Tweet(tweet.text)
                #pre process the tweet to match the word2vec module 
                currentTweetTokens = currentTweet.getTokens()
                if len(currentTweetTokens) > 0:
                    user_tweets.append( ' '.join(currentTweetTokens)) 

            print("Loop Range:",(max_tweets_num - (max_tweets_num % 200))// 200)
            for i in range(0, 1 + ((max_tweets_num - (max_tweets_num%200)) // 200 )):
                if len(recent_tweets) > 0:
                    time.sleep(.3)
                    #update the id of the oldest tweet less one
                    oldest_id = recent_tweets[-1].id - 1
                    #all subsiquent requests use the max_id param to prevent duplicates
                    recent_tweets = self.__twitter_api.user_timeline(screen_name = self.user_name,count=200,max_id=oldest_id)
                    print("Recent tweets len:",len(recent_tweets))

                    for tweet in recent_tweets:
                        currentTweet = Tweet(tweet.text)
                        #pre process the tweet to match the word2vec module 
                        currentTweetTokens = currentTweet.getTokens()
                        if len(currentTweetTokens) > 0:
                            user_tweets.append( ' '.join(currentTweetTokens)) 
        except Exception as e:
            print(str(e))
            return user_tweets            
        return user_tweets

# user_name = raw_input("enter user name")
# max_tweets = raw_input("enter max tweets num ")
# tc = TwitterFetcher(user_name)
# tc.do_task(int(max_tweets))                
