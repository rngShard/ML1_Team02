from compass import PoliticalCompass
from Twitter_fetcher import TwitterFetcher

list_of_user_names = []
max_tweets_num = 500

with open("user_names.txt","r") as user_names_file:
    user_names = user_names_file.readlines()
    list_of_user_names = user_names


probalities_vec = []
for user_name in list_of_user_names:
    tc = TwitterFetcher(user_name)
    tc.do_task(int(max_tweets_num))
    tweets_file_name = user_name +".txt"
    user_probalites = []
    #open the file that contains the tweets
    #TODO : call function to get  user_probalites
    probalities_vec.append(user_probalites)

#plot the compass 
p = PoliticalCompass()
p.plotPoliticianInCompass(list_of_user_names, probalities_vec)