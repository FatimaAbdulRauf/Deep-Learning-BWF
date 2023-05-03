data = [
    {'price': 850000, 'rooms': 4, 'neighborhood': 'Queen Anne'},
    {'price': 700000, 'rooms': 3, 'neighborhood': 'Fremont'},
    {'price': 650000, 'rooms': 3, 'neighborhood': 'Wallingford'},
    {'price': 600000, 'rooms': 2, 'neighborhood': 'Fremont'}
]

#ndicating the presence or absence of a category with a value of 1 or 0
from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse=False, dtype=int)
print(vec.fit_transform(data))
print(vec.get_feature_names_out())

vec = DictVectorizer(sparse=True, dtype=int)
print(vec.fit_transform(data))

#word counts--- convert text to representative numerical values
sample = ['problem of evil',
          'evil queen',
          'horizon problem']
from sklearn.feature_extraction.text import CountVectorizer

new_vec = CountVectorizer()
X = new_vec.fit_transform(sample)
import pandas as pd
print(pd.DataFrame(X.toarray(), columns=new_vec.get_feature_names_out()))