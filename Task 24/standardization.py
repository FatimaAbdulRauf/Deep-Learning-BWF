from sklearn import preprocessing
import numpy as np

X_train = np.array([[ 1., -1.,  2.],
                     [ 2.,  0.,  0.],
                     [ 0.,  1., -1.]])
scaler = preprocessing.StandardScaler().fit(X_train)
print(scaler.mean_)
print(scaler.scale_)

X_scaled = scaler.transform(X_train)
print(X_scaled)

#scaled data has zero mean and unit variance
print(X_scaled.mean(axis=0))
print(X_scaled.std(axis=0))
