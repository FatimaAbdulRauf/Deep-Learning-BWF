import pandas as pd
import numpy as np
from numpy import nan as NA

data = pd.DataFrame({"m1":["one", "two"]*3 +["two"],\
                     "m2":[1,1,2,3,3,4,4] })

print(data)
print(data.duplicated())
print(data.drop_duplicates())

data["v1"] = range(7)
print(data.drop_duplicates(["m1"], keep="last"))