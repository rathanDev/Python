import numpy as np
import pandas as pd 

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
# print(df)

# print()

# w = df['W']
# w = df.W

# wz = df[['W','Z']]

# new = df['new']

df['new'] = df['W'] + df['Y']

print(df)
print()

# droppedNew = df.drop('new', axis=1)
# print(droppedNew)

# dropped_e = df.drop('E')
# print(dropped_e)

# print(df.shape)

# row_a = df.loc['A']

# row_c = df.iloc[2]
# print(row_c)

# by = df.loc['B','Y']

ab_wy = df.loc[['A','B'],['W','Y']]

print(ab_wy)







