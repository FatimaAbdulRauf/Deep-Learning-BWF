from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split

iris = load_iris()
print(iris.feature_names)

df = pd.DataFrame(iris.data, columns = iris.feature_names)
print(df.head)
df['target'] = iris.target

df['flower_name'] =df.target.apply(lambda x: iris.target_names[x])
df0 = df[:50]   #setosa
df1 = df[50:100]    #versicolor
df2 = df[100:]  #virginica

x = df.drop(['target', 'flower_name'], axis='columns')
y = df.target

x_train, x_test, y_train, y_test = train_test_split(x,y, \
                                    test_size=0.2, random_state=1)
print(len(x_train))
print(len(x_test))

knn = KNeighborsClassifier(n_neighbors=10)
print(knn.fit(x_train, y_train))
print(knn.score(x_test, y_test))
print(knn.predict_proba(x_test))

