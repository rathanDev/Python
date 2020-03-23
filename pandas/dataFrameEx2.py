import numpy as np
import pandas as pd 

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'],['W','X','Y','Z'])

print(df)

print()

# conditional selection

# bool_df = df > 0;

# print(bool_df)

# into = df[bool_df]
# print(into)


boolserW = df['W'] > 0
print(boolserW)

boolserY = df['Y'] > 1
print(boolserY)

print(df[boolserW boolserY])








