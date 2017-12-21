'''Import data from vectors.csv in proper format.'''
import pandas as pd
import re

re_str_to_array = re.compile('array\(\[([\s\S]*?)\]')

path_to_file = "./vectors.csv"
chunksize = 10 ** 2

for chunk in pd.read_csv(path_to_file, chunksize=chunksize):
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
                                                                                
    print df.tail(), df.shape
                                                                                        
    break
