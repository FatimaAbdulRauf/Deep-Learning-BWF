import pandas as pd
import glob
from numpy import nan as NA

#glob to get csv files
path = r"C:\Users\LC\OneDrive\Documents\BTW Deep Learning\Project\US_Census Data Cleaning\*.csv"
csv_files = glob.glob(path)

#empty list for dataframes
frame_list = []

for filename in csv_files:
    df = pd.read_csv(filename)
    df.head()
    frame_list.append(df)

us_census = pd.concat(frame_list, ignore_index= True)
us_census['TotalPop'] = us_census['TotalPop'].astype('int64')
us_census['Income'] = us_census['Income'].str.replace("$","")
us_census['Income'] = us_census['Income'].astype("float64")
columns = ["Hispanic", "White", "Black", "Native", "Asian", "Pacific"]
for col in columns:
    us_census[col] = us_census[col].str.replace("%", "")
    us_census[col] = us_census[col].astype("float64")
us_census = us_census.fillna(0)
print(us_census['Pacific'])
print(us_census.dtypes)



