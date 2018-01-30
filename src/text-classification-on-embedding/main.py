from compass import PoliticalCompass
from Twitter_fetcher import TwitterFetcher
from test_tweet_list import evaluateFile
import numpy as np
import compass

list_of_user_names = []
max_tweets_num = 200
max_fetched_users = 25

party_name=['csu', 'fdp', 'afd', 'gruene', 'die-linke', 'spd', 'cdu']
party_name_index=[0,1,2,3,4,5,6]

current_index = 6

with open("test_users/"+party_name[current_index]+".txt", 'r+') as f:
    list_of_user_names = list(f.read().splitlines())

probalities_vec = []
party_index= []
fetched_user_names = []
correct_users = 0
fetched_users = 0
total_users = len(list_of_user_names)
for user_name in list_of_user_names:
    print("User Name: ", user_name, "$$")
    tc = TwitterFetcher(user_name)
    tc.do_task(int(max_tweets_num))
    tweets_file_name = "output/"+user_name+".txt"
    #print(tweets_file_name)
    with open(tweets_file_name, 'r+') as f:
        tweet_lines = list(f.read().splitlines())
        if len(tweet_lines) > 0 :
            user_probabilities = evaluateFile(tweets_file_name)
            #open the file that contains the tweets
            #TODO : call function to get  user_probalites
            probalities_vec.append(user_probabilities)
            fetched_user_names.append(user_name)
            party_index = np.argmax(user_probabilities)
            fetched_users += 1
            if party_index == party_name_index[current_index]:
                correct_users += 1
            if fetched_users >= max_fetched_users:
                break
        else:
            total_users -= 1
accuracy = (correct_users / fetched_users) * 100
print("Total users", fetched_users)
print("Users correctly identified", correct_users)
print("The accuracy for team "+party_name[current_index]+":", accuracy)

# plot the compass 
for i in range(0, len(fetched_user_names)):
	compass.plot_user(party_name[current_index], fetched_user_names[i], probalities_vec[i])
#p = PoliticalCompass().plotPoliticianInCompass("afd",fetched_user_names, probalities_vec)
'''The Target Names:  [0:'csu', 1:'fdp', 2:'afd', 3:'gruene', 4:'die-linke', 5:'spd', 6:'cdu']'''
     
