import numpy as np
import pandas as pd

d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)
print(df)


# df = df.dropna(axis=1)

print('----- -----')

# ddf = df.dropna(thresh=2)

f = df.fillna(value='FILL VAL')

print(f)
# print(ddf)




