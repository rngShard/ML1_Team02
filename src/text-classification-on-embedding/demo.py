from Tkinter import *
from Twitter_fetcher import TwitterFetcher
from test_tweet_list import evaluateFile
import compass
import tkMessageBox

def show_entry_fields():
    tc = TwitterFetcher(e1.get())
    tc.do_task(200)
    tweets_file_name = "output/"+e1.get()+".txt"
    #print(tweets_file_name)
    with open(tweets_file_name, 'r+') as f:
        tweet_lines = list(f.read().splitlines())
        if len(tweet_lines) > 0 :
            user_probabilities = evaluateFile(tweets_file_name)
            compass.plot_user('dummy_name', e1.get(), user_probabilities)
        else:
            tkMessageBox.showinfo("Error", "No valid Tweets found")

master = Tk()
master.title('Political Classifier')
Label(master, text="Twitter user_name").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='classify', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )