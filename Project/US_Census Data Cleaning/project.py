import pandas as pd
import glob
from numpy import nan as NA
import matplotlib.pyplot as plt

#glob to get csv files
path = r"C:\Users\LC\OneDrive\Documents\BTW Deep Learning\Project\US_Census Data Cleaning\*.csv"
csv_files = glob.glob(path)

#empty list for dataframes 
frame_list = []

for filename in csv_files:
    df = pd.read_csv(filename)
    df.head()
    frame_list.append(df)

#concatenating all files
us_census = pd.concat(frame_list, ignore_index= True)

#replacing unwanted characters and changing datatypes
us_census['TotalPop'] = us_census['TotalPop'].astype('int64')
us_census['Income'] = us_census['Income'].str.replace("$","")
us_census['Income'] = us_census['Income'].astype("float64")

#using list to remove % from the race columns and changing their datatype
columns = ["Hispanic", "White", "Black", "Native", "Asian", "Pacific"]
for col in columns:
    us_census[col] = us_census[col].str.replace("%", "").astype("float64")
    
#removing NaN values
us_census = us_census.fillna(0)

#splitting GenderPop into two new columns Men and Women
us_census[['Men', 'Women']] = us_census['GenderPop'].str.split("_", expand=True)
us_census['Men'] = us_census['Men'].str.replace("M","")
us_census['Women'] = us_census['Women'].str.replace("F","")

#replacing empty string to NaN value so it can be converted to numerical value
us_census['Women'] = us_census['Women'].replace('', NA)
us_census['Men'] = us_census['Men'].astype("int")

#using TotalPop-Men to fill NaN values for Women
us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop']\
    -us_census['Men']).astype("int")

#removing duplicates
us_census.drop_duplicates()

#scatter plot for Women and Income
plt.scatter(us_census['Women'], us_census['Income'])
plt.xlabel('Average Income')
plt.ylabel('Number of Women')
plt.show()

#histogram of races
plt.hist([us_census['Hispanic'],us_census['White'],us_census['Black'],\
            us_census['Native'],us_census['Asian'],us_census['Pacific']],\
            bins=10, color=['blue','red','green','yellow','black','purple'],\
            label=['Hispanic', 'White', 'Black', 'Native', 'Asian','Pacific'])
              
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.title('Histogram of Races in US Census')
plt.legend()
plt.show()
