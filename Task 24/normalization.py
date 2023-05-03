from sklearn import preprocessing

X = [[ 1., -1.,  2.],
      [ 2.,  0.,  0.],
      [ 0.,  1., -1.]]
X_normalized = preprocessing.normalize(X, norm='l2')
print(X_normalized)

normalizer = preprocessing.Normalizer().fit(X)  # fit does nothing
print(normalizer)

print(normalizer.transform(X))
print(normalizer.transform([[-1.,  1., 0.]]))