import numpy as np
import pandas as pd


# labels = ['a','b','c']
# my_data = [10,20,30]
# arr = np.array(my_data)
# d = {'a':10, 'b':20, 'c':30}

# ser = pd.Series(data=my_data)

# ser = pd.Series(data=my_data, index=labels)

# ser = pd.Series(my_data, labels)

# ser = pd.Series(arr)

# ser = pd.Series(d)

# ser = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])

ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
print(ser1)

ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)

val = ser1['USA']
print(val)

s_sum = ser1 + ser2
print(s_sum)




