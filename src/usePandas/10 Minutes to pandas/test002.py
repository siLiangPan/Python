# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
df = pd.DataFrame(data=np.random.randn(1000, 4), index=ts.index,
                  columns=['A','B','C','D'])
    
B = []
for i in range(1000):
    if i < 100:
        #B.append(np.nan)
        B.append(1)
    else:
        B.append(df.at[ts.index[i-100],'A'])
#print(B)
df['B'] = B
df = df.cumsum()
#plt.figure()
print(ts.index)
df.plot()
plt.legend(loc='best')
plt.show()