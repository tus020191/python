from numpy import *
from pandas import *
"""
a=random.randint(1,10,14)
print(where(a%3==0))
print(a.take([3,6,9,12]))
a.value_counts()
b=Series(random.randint(1,10,35))
print(concat([b,a],axis=1))
print(a.value_counts())
"""
a=Series(random.randint(1,12,6),index=['c','b','a','d','e','j'])
print(a)
print(a.sort_index())
print(a.sort_index(ascending=False))
print("")
d=DataFrame(a.values.reshape(3,-1),columns=['a','b'])
print(d)
print(d.sort_index(ascending=False))
print(d.sort_index(axis=1,ascending=False))
print(d.sort_index(by='b'))