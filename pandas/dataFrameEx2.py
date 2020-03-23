import numpy as np
import pandas as pd 

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'],['W','X','Y','Z'])
print('DataFrame \n', df)

big_w = df['W'] > 0;
big_w_df = df[big_w]

print('CoditionalSelection\n', big_w)
print('\n', big_w_df) 

big_w_yz = df[df['W']>0][['Y','Z']]
print('SelectCols\n', big_w_yz)

# conditional selection

# bool_df = df > 0;

# print(bool_df)

# into = df[bool_df]
# print(into)


boolserW = df['W'] > 0
# print(boolserW)

boolserY = df['Y'] > 1
# print(boolserY)

WandY = df[boolserW & boolserY]

# print('W and Y', WandY)

w_or_y = df[((df['W'] > 0) | (df['Y']))]
# print('W or Y', w_or_y)



df_index_reset = df.reset_index()
print('Index Reset \n', df_index_reset)


new_ind = 'BT TR VA MA PE'.split()
print('New Index \n', new_ind)

df['States'] = new_ind

df.reset_index()
df.set_index('States')

print('DataFrame \n', df)











