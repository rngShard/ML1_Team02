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
            if not word.startswith("http") and not word.startswith("@"): 
                words.append(word.lower())
        return words