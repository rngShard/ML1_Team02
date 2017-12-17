# -*- coding: utf-8 -*- 

import re
class Tweet:
    def __init__(self,tweet):
        if tweet is not None:
            self.tweet=tweet
        else:
            self.tweet = []    
    # returns list of tokens in the tweet after removing links, mentions
    def getTokens(self):
        words = []
        for word in self.tweet:
            #neglect urls, and mentions in tweet
            if not word.startswith("http") and not word.startswith("@"):
                word = word.lower()
                #remove special characters, and keep special german characters
                re.sub('r[^A-Za-z0-9äöüßẞÜÖÄ]+', '', word) 
                words.append(word)
        return words