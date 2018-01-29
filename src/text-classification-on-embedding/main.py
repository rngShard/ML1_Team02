from compass import PoliticalCompass
from Twitter_fetcher import TwitterFetcher
from test_tweet_list import evaluateFile
import numpy as np

list_of_user_names = []
max_tweets_num = 700


with open("user_names", 'r+') as f:
    list_of_user_names = list(f.read().splitlines())

probalities_vec = []
party_index= []
correct_users = 0 
total_users = len(list_of_user_names)
for user_name in list_of_user_names:
    print("User Name: ", user_name, "$$")
    tc = TwitterFetcher(user_name)
    tc.do_task(int(max_tweets_num))
    tweets_file_name = "output/"+user_name+".txt"
    #print(tweets_file_name)
    with open(tweets_file_name, 'r+') as f:
        tweet_lines = list(f.read().splitlines())
        if len(tweet_lines) > 0:
            user_probabilities = evaluateFile(tweets_file_name)
            #open the file that contains the tweets
            #TODO : call function to get  user_probalites
            probalities_vec.append(user_probabilities)
            party_index = np.argmax(user_probabilities)
            if party_index == 3:
                correct_users += 1
        else:
            total_users -= 1
accuracy = (correct_users / total_users) * 100
print("Total users", total_users)
print("Users correctly identified", correct_users)
print("The accuracy for team cdu:", accuracy)

# plot the compass 
p = PoliticalCompass().plotPoliticianInCompass(list_of_user_names, probalities_vec)
'''The Target Names:  [0:'csu', 1:'fdp', 2:'afd', 3:'gruene', 4:'die-linke', 5:'spd', 6:'cdu']'''
     
