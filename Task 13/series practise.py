import pandas as pd
from pandas import Series

obj = pd.Series([3, 4, 8, 9])
print(obj)
print(obj.index)

obj2 = pd.Series([2,3,4,5], index=["a", "b", "c", "d"])
print(obj2.index)
print(obj2[["c", "a", "d"]])
print(obj2[obj2>3])
print(obj2 * 2)
print("b" in obj2)

dict1 = {"Ohio": 35000, "Texas": 71000, "Oregan": 16000, "Utah": 5000}
obj3 = pd.Series(dict1)
print(obj3)

states = ["California", "Ohio", "Oregan", "Texas"]
obj4 = pd.Series(dict1, index= states)
print(obj4)
print(pd.notnull(obj4))
print(obj3+obj4)

obj4.name = "population"
obj4.index.name = "state"
print(obj4)

