import re
import os
import csv
import tweepy
import time

#used to extract politations data from the data input file, crawle tweets, and save them to CSV file
class TweetsCrawler:
    #input_data_file : path to the the input file contains politicians' data
    def __init__(self, input_file_path, output_csv_file_name):
        self.__input_file_path = input_file_path
        self.__output_csv_file_name = output_csv_file_name
        #twitter app access tokens
        __consumer_key = "TcoDRSehIlGkWfxM0uXADVVKN"
        __consumer_secret = "u343Uv4Ta54zoHp5PALoXd5fYpSVhSfynUqqAQVwsn3cMtriPD"
        __access_key = "939464114606346240-rdJ9A9I4XuW76R2ClHLuBDtiImRWT0h"
        __access_secret = "JDbzppXonkV52rbG2pJcx92p1L0BuR8Xaz8dh3nEsPK8f"
        #initialize the twitter API
        auth = tweepy.OAuthHandler(__consumer_key, __consumer_secret)
        auth.set_access_token(__access_key, __access_secret)
        self.__twitter_api = tweepy.API(auth)
    
    #main function of the class, it gets all politiacians tweets, and writes the results to output csv file
    def do_task(self):      
        politicians_data = self.__parse_input_file()
        remaining_number =len(politicians_data)
        with open(self.__output_csv_file_name, 'wb') as out_csv:
            csv_writer = csv.writer(out_csv)
            csv_writer.writerow(["politician_name", "party", "tweeted_at", "tweet"])
            for politician in politicians_data:
                output_data = []
                #sleep for .6s to avoid twitter api rate limit
                time.sleep(.6)
                try:
                    politician_tweets = self.__get_user_tweets(politician[-1])
                    for tweet in politician_tweets:
                        output_data.append([politician[0], politician[1], tweet[0], tweet[1]])
                        #write output_data to output csv file 
                        csv_writer.writerows(output_data)
                except:
                    print "error getting tweets for politician_name: %s" %   politician[0]      

                remaining_number-=1
                print remaining_number

    #parses the input data file, and returns list of [politiacian_name, party_name, twitter_user_name]
    def __parse_input_file(self):
        politicians_data = []
        with open(self.__input_file_path) as input_file:
            #each line is in the following format : politician_name part_name twitter_account_link
            for line in input_file:
                tokens = line.split()
                #take only user_name from twitter_link (last token)
                match = re.search(r'.*twitter.com/(.*)$',tokens[-1])
                #capture only twitter user name using Regex
                tokens[-1] = match.group(1)

                politicians_data.append(tokens[1:])
        return politicians_data

    #returns most recent 200 tweets of given user_name. 
    #note : we can increase the number of tweets till 3240
    def __get_user_tweets(self,user_name):
        user_tweets = []
        #for now we set the max number of tweets to get to 200
        recent_tweets = self.__twitter_api.user_timeline(screen_name = user_name, count = 200)
        for tweet in recent_tweets:
            user_tweets.append([tweet.created_at, tweet.text.encode("utf-8")])

        return user_tweets


tc = TweetsCrawler("data.txt","train.csv")
tc.do_task()                