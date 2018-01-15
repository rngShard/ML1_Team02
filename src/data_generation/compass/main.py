from compass import PoliticalCompass
from Twitter_fetcher import TwitterFetcher

#TODO : read user_names from file, and put them to this list
list_of_user_names = ["fkfsldk", "fjasjfkjkaljk", "sjafksajkfjkaj"]
max_tweets_num = 500

probalities_vec = []
for user_name in list_of_user_names:
    tc = TwitterFetcher(user_name)
    tc.do_task(int(max_tweets))
    tweets_file_name = user_name +".txt"
    user_probalites = []
    #open the file that contains the tweets
    #TODO : call function to get  user_probalites
    probalities_vec.append(user_probalites)

#plot the compass 
p = PoliticalCompass()
p.plotPoliticianInCompass(list_of_user_names, probalities_vec)