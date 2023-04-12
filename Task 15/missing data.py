import pandas as pd
import numpy as np
from numpy import nan as NA

color_data = pd.Series(["Viridian", "Cobalt Blue", "Vermillion Red",\
                         np.nan, "Titanium White"])
print(color_data)
print(color_data.isnull())

color_data[0] = None
print(color_data.isnull())

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [NA, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
print(df.dropna())

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],\
 [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
print(data)
print(cleaned)
