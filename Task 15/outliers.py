import pandas as pd
import numpy as np
from numpy import nan as NA

data = pd.DataFrame(np.random.randn(1000,4))
print(data.describe())

col = data[2]
print(col[np.abs(col) > 3])

print(data[(np.abs(data)>3).any(1)])