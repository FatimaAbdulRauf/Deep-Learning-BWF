import pandas as pd
import numpy as np
from numpy import nan as NA

data_num = pd.DataFrame(np.random.randn(7,3))
data_num.iloc[:4,1] = NA
data_num.iloc[:2,2] = NA

print(data_num)
print(data_num.dropna(thresh=2))

data_num.fillna({1:0.5,2:0})

_ = data_num.fillna(0, inplace=True)
print(data_num)

data = pd.Series([1.,NA,3.6,NA,7])
data.fillna(data.mean())
data.replace(1, NA)
print(data)