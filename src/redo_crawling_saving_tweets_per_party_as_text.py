import pandas as pd
import re

PATH_TO_FILE = "./tweetsCrawler/train.csv"
CHUNKSIZE = 10 ** 3

RESULT_PATH = "./party_csvs/"
dfs_by_parties = {}

df = pd.read_csv(PATH_TO_FILE)

for party in df['party'].unique():
    if party not in dfs_by_parties:
        dfs_by_parties[party] = []
    sngl_party_df = df.loc[df['party'] == party]
    dfs_by_parties[party].append(sngl_party_df.drop('party', 1))

# concatinate and save to csv
for party in dfs_by_parties:
    dfs_x = pd.concat(dfs_by_parties[party])
    print 'Saving to disk as CSV:', party
    print '... with Shape: ', dfs_x.shape
    dfs_x.to_csv(RESULT_PATH + party+'.csv', index=False, header=False)
