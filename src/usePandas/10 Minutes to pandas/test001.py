# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

# Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:
#dates = pd.date_range(start, end, periods, freq, tz, normalize, name, closed)
dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(data=np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
#print(df.head()) # 默认5行
#print(df.tail(3)) # 默认5行
# Display the index, columns, and the underlying numpy data
#df.index
#df.columns
#df.values

# Describe shows a quick statistic summary of your data
print(df.describe())
# Transposing your data 矩阵转置
print(df.T)

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#print(ts)
ts = ts.cumsum()
#print(ts)
#print(ts.plot())
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
#plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()
'''
#Creating a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })
print(df2)
'''