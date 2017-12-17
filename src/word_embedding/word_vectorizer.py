# used to convert list of N tokens to a N*d matrix
class WordVectorizer:
    def __init__(self,word2vecModule):
        self.word2vecModule = word2vecModule

    # for a given list of words, the function will return a N*d matrix, where each row is a word vector
    #note: if some word doesn't exist in the word2vec module, its vector will not appear in the output matrix
    #so we can have row numbers less than N
    def getMatrix(self,words):
        wordVecs =[]
        #for testing return percentage of not found words in the given list
        percentOfNotFounds = 0
        for word in words:
            if word in self.word2vecModule:
                wordVecs.append(self.word2vecModule[word])
            else:
                percentOfNotFounds+=1
        if len(words) > 0:
            percentOfNotFounds = percentOfNotFounds/len(words)
        else:
            percentOfNotFounds =1
        return wordVecs, percentOfNotFounds*100
