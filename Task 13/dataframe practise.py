import pandas as pd
import numpy as np
from pandas import DataFrame

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
 'year': [2000, 2001, 2002, 2001, 2002, 2003],
 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data, columns = ["year", "state", "pop", "debt"])
print(frame)
print(frame.year)
frame["debt"] = np.arange(6.)
print(frame)
del frame["debt"]
print(frame)