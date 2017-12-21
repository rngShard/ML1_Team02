import pandas as pd
import re

re_str_to_array = re.compile('array\(\[([\s\S]*?)\]')

path_to_file = "./vectors.csv"
chunksize = 10 ** 2

for chunk in pd.read_csv(path_to_file, chunksize=chunksize):
    df = chunk
    # transform string-valued vector matrix into proper numerical matrix
    proper_numerical_matrices = []
    for mat_str in df.loc[:,'matrix']:
        mat_num = [[float(x) for x in row.split(',')] for row in re_str_to_array.findall(mat_str)]
        proper_numerical_matrices.append(mat_num)
    proper_mat_num_col = pd.Series(proper_numerical_matrices, name='matrix', index=range(chunksize))
    df = pd.concat([df.drop('matrix',1), proper_mat_num_col], axis=1)
    print df.head()
                                                      
    break
