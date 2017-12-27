'''Import data from vectors.csv in proper format.

Then runs through chunks, accumulating records on a per-party basis
and ultimately concatinates them to single CSV-files per party. 
'''
import pandas as pd
import re

re_str_to_array = re.compile('array\(\[([\s\S]*?)\]')

PATH_TO_FILE = "./vectors.csv"
CHUNKSIZE = 10 ** 3

RESULT_PATH = "./party_csvs/"
dfs_by_parties = {}


# Display global parameters
print "Path to initial file:", PATH_TO_FILE
print "Path to output:", RESULT_PATH 
print "Chunksize:", CHUNKSIZE


# Run over chunks and transform values + accumulate into dict
for i, chunk in enumerate(pd.read_csv(PATH_TO_FILE, chunksize=CHUNKSIZE)):
    print 'Reading chunk #', i
    df = chunk

    # if value of percentageOfMissingWords (naming is not quite correct) is 100 then the tweet contains no valid input text
    df = df[df.percentageOfMissingWords != 100].reset_index(drop=True)    # don't forget "reset_index", won't work otherwise!!
                        
    # transform string-valued vector matrix into proper numerical matrix
    proper_numerical_matrices = []
    for mat_str in df.loc[:,'matrix']:
        mat_num = [[float(x) for x in row.split(',')] for row in re_str_to_array.findall(mat_str)]
        proper_numerical_matrices.append(mat_num)
    proper_mat_num_col = pd.Series(proper_numerical_matrices, name='matrix_num', index=range(df.shape[0]))
    df = pd.concat([df, proper_mat_num_col], axis=1)
                                                                    
    # clean columns not needed anymore
    df = df.drop('matrix', 1).drop('percentageOfMissingWords', 1)
                                        
    #! now comes the splitting and saving
    df = df.sort_values('party', axis=0)
    for party in df['party'].unique():
        if party not in dfs_by_parties:
            dfs_by_parties[party] = []
        sngl_party_df = df.loc[df['party'] == party]
        dfs_by_parties[party].append(sngl_party_df)
    
    if i % 5 == 0:
        print "<< Status-Update >>"
        for party in dfs_by_parties:
            print 'Len of <'+party+'>:', len(dfs_by_parties[party])
    
      # For testing / debugging purposes
    if i > 15:
        break


# concatinate and save to csv
for party in dfs_by_parties:
    dfs_x = pd.concat(dfs_by_parties[party])
    print 'Saving to disk as CSV:', party
    print '... with Shape: ', dfs_x.shape
    dfs_x.to_csv(RESULT_PATH + party+'.csv', index=False)
