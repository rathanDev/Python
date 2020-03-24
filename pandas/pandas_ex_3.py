
# Index hierarchy, Multi level index

import numpy as np
import pandas as pd

from numpy.random import randn

print('Constructing Multi Index DataFrame')

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_zip = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_zip)

print('Outside\n', outside)
print('Inside\n', inside)
print(hier_zip)
print(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print('DataFrame\n', df)

g1 = df.loc['G1']
print(g1)

df.index.names = ['Groups', 'Nums']
print(df.index.names)