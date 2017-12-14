#a simple script to show how to load, and use the word2vec module
import os 
import gensim

# you can download the folder that contains the module from here https://spinningbytes.com/resources/embeddings/
module = gensim.models.KeyedVectors.load_word2vec_format('./embed_tweets_de_200M_200D/embedding_file',binary=False)

# print the 200 dimensions vector for all the german words I know :)  
print module['frau']
print module['abend']
print module['tag']

#similarity between two words
print model.similarity('mann','frau')