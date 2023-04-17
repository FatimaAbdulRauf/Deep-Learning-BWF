from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf1 = tree.DecisionTreeClassifier()
clf1 = clf1.fit(X, Y)
print(clf1.predict([[2.,2.]]))
print(clf1.predict_proba([[2.,2.]]))

iris = load_iris()
Z, p = iris.data, iris.target
clf = tree.DecisionTreeClassifier()
clf = clf.fit(Z, p)
tree.plot_tree(clf)

decision_tree = DecisionTreeClassifier(random_state=0, max_depth=2)
decision_tree = decision_tree.fit(iris.data, iris.target)
r = export_text(decision_tree, feature_names=iris['feature_names'])
print(r)