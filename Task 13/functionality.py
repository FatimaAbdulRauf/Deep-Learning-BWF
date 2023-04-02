import pandas as pd
from pandas import Series, DataFrame

obj = pd.Series([4,5,6,7], index=["d", "c", "b", "a"])
print(obj)

obj2 = obj.reindex(["a", "b", "c", "d", "e"])
print(obj2)

new_obj = obj2.drop("c")
print(new_obj)
print(obj2.loc["a"])
print(obj.iloc[[1,2]])
print(obj.sort_index())
print(obj.rank(ascending= True))