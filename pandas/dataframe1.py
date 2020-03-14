import numpy as np
import pandas as pd 
from numpy.random import randn

np.random.seed(102)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

# w = df['W']
# print(type(w))

# df['new'] = df['W'] + df['Y']

# print(df)

# df.drop('new',axis=1,inplace=True)
# print(df)

# df.drop('E',axis=0)


# print(df)

# z = df[['Z','X']]

# print(z)

# a = df.loc['A']
# print(a)

# i = df.iloc[2]
# print(i)

# ab = df.loc[['A','B'],['W','Y']]
# print(ab)

# b0 = df[df['W']>0][['Y','X']]
# df = df[df['W']>0][df['Y']>0]
# print(b0)

# bool_ser = df['W']>0
# print(bool_ser)

# df['bool_ser'] = bool_ser

# print(df)

# df.drop('bool_ser',axis=1,inplace=True)

# bw = df[df['W']>0]
# by = df[df['Y']>0]

# df[(bw) & (by)]

# bwby = df[(df['W']>0) & (df['Y']>0)]

# print(bwby)

# ri = df.reset_index()
# print(ri)

new_ind = 'CA NY WY OR CO'.split()
# print(new_ind)

df['States'] = new_ind

# df.reset_index()

sdf = df.set_index('States')

# print(sdf)

# print(df.shape)

# ----- ----- #

outside = 'G1 G1 G1 G2 G2 G2'.split()
# print(out)

inside = [1,2,3,1,2,3]
# print(inside)

hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# print(hier_index)


# df = pd.DataFrame(randn(6,2), hier_index, ['A','B'])
# print(df)

# dg1 = df.loc['G1'].loc[1]
# print(dg1)

# gg = df.loc['G2'].loc[2]['A']
# print(gg)

print(df)













