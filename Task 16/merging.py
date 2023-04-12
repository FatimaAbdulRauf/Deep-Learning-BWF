import pandas as pd

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],\
 'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],\
 'data2': range(3)})

print(pd.merge(df1,df2, on="key", how="left"))

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

print(pd.merge(left1,right1,left_on="key", right_index=True, how="outer"))


s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
print(pd.concat([s1,s2,s3]), axis=1)
