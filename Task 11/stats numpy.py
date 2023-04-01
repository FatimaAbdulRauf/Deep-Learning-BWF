import numpy as np

practise = np.array([[ 2.1695, -0.1149, 2.0037, 0.0296],
 [ 0.7953, 0.1181, -0.7485, 0.585 ],
 [ 0.1527, -1.5657, -0.5625, -0.0327],
 [-0.929 , -0.4826, -0.0363, 1.0954],
 [ 0.9809, -0.5895, 1.5817, -0.5287]])

print("Mean: ", practise.mean())
print("Median", np.median(practise))

print("Mean across the columns: ", practise.mean(axis=1))
print("Mean down the rows: ", practise.mean(axis=0))

print("Cummulative sum across coulmns: ", practise.cumsum(axis=1))
print("Cummulative sum down rows: ", practise.cumsum(axis=0))

print("Cummulative product: ", practise.cumprod())

print("Standard deviation: ", practise.std())
print("Variance: ", practise.var())

first_quantile = np.quantile(practise, 0.25)
second_quantile = np.quantile(practise, 0.5)
third_quantile = np.quantile(practise, 0.75)
print("First quantile: ", first_quantile)
print("Second quantile ", second_quantile)
print("Third quantile ", third_quantile)
print("Interquartile Range: ", third_quantile - first_quantile)
