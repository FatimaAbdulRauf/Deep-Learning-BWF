import timeit
"""def addition():
    print('Addition', sum(range(100)))
n= 5
result = timeit.timeit(stmt='addition()', globals=globals(), number=n)
print(f"Execution time is {result/n}seconds")

a=[]
r1= timeit.timeit(stmt='a', globals=globals(), number=1)
print(r1)
b = list()
r2= timeit.timeit(stmt='b', globals=globals(), number=1)
print(r2)"""

def for_loop():
    for i in range(10):
        print(i)
loop = [x for x in range(10)]
r2= timeit.timeit(stmt='for_loop', globals=globals(), number=1)
r3= timeit.timeit(stmt='loop', globals=globals(), number=1)
print("Using function the time for code execution is:", r2, "seconds","\n"\
    "Using list comprehension we get:", r3, "seconds")