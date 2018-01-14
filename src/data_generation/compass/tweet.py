# -*- coding: utf-8 -*- 

import re
class Tweet:
    def __init__(self,tweet):
        if tweet is not None:
            self.tweet=tweet
        else:
            self.tweet = ""   
    # returns list of tokens in the tweet after removing links, mentions, retweet header
    def getTokens(self):
        #remove retweet header (retweet starts with RT)
        self.tweet = re.sub("^RT ","",self.tweet)
        words = []
        for word in self.tweet.split():
            #neglect urls, and mentions in tweet
            if not word.startswith("http") and not word.startswith("@"):
                word = word.lower()
                #remove special characters, and keep special german characters
                word = re.sub('[^A-Za-z0-9äöüßẞÜÖÄ]+', '', word) 
                #convert capital german special chars to lower also
                word = re.sub('Ä', 'ä', word)
                word = re.sub('Ö', 'ö', word)
                word = re.sub('Ü', 'ü', word)
                word = re.sub('ẞ', 'ß', word)
                if len(word)>0:
                    words.append(word)
        return words
