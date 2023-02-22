import numpy as np
import pandas as pd
"""
a=pd.Series([1 ,2,3 ,4,5,6,np.nan,7,8,9,10])
print(a)
print(a.drop((4))) # returns another  series by removing given index ,no change in oringinal series 

print(a.reindex([9,8,7,6,5,3,4,1,2,0])) # returns another series having index in given specific order , no change in original series 

print(a.sort_index(ascending=False))
print(4 in a ) #tells whether given index is in series or not 
print(a>5)
print(a[a>5])
"""
b=pd.Series([-2,1,2,4,7,5,3,4,6,7,2,3,9,1,1,1,1,8,3,2,8,9,7,5,6,4,3,7,4,5,6,5,5,5,5,5,6])
#print(a+b)
#print(b)
#print(b.rank())#by default method is average
#print(b.rank(method='first'))
#print(b.rank(method='max'))
#print(b.rank(method='average'))
#print(b.rank(method='min'))

d=pd.DataFrame({1:{"jaipur":"a","delhi":"b"},2:{"jaipur":"c","delhi":"d"}})

#print(d)
e=pd.DataFrame(np.arange(25).reshape(5,5),columns=list("abcde"),index="jaipur delhi gujrat punjab kerala".split())
#print(e)
#print(e.values)
#print(e.index)
#print(e.columns)
#e.columns=list("edcba")
#print(e)
#e.index=["jai","del","guj","pjn","kr"]
#print(e)
#print(e[1:4])
#print(e.drop(("del")))#no change in e instead it return another dataframe by removing del index from e 
#print(e)

f=pd.DataFrame(e)
f.index=[1,2,3,4,5]
#print(f)
#print(f.reindex([2,3,4,5,1,1.3,2.5,4.5,2.3,5.6],method="ffill"))

#print(f.reindex(columns=list("ag"),method='ffill'))#no change in f 
#print(f)
#print(f.sort_index(ascending=False))
#print(f.sort_values(by='a'))
#print(f)


#s1=pd.Series(f["a"])
#print(s1)
g=pd.DataFrame(np.array([-1,0,2,3,4,6,8,3,9,5,4,7,11,6,12,9]).reshape(4,4))
#print(g,'\n',g.rank())


"""

df=pd.DataFrame([[1,2],[np.nan,4],[5,np.nan]],columns=["one","two"],index=list("abc"))

print(df)
print("")

print(df.sum())
print("")
print(df.sum(skipna=False))#not ignore nun value
print("")
print(df.sum(axis=1))
print("")

print(df.max())
print(df.max(axis=1,skipna=False))

print(df.count(axis=1))
print(df.cumsum())
print(df.cummax())
print(df.cummin())

"""

"""
df1=pd.DataFrame([[1,2],[3,4],[5,6]],columns=["one","two"],index=list("abc"))


print(df1)
print(df1.cumsum())
print(df1.cummin())
print(df1.cummax())

"""
"""
print(b)

print(b.unique())
print(pd.unique(b.values))

print(b.value_counts(sort=True))

print(b.value_counts(sort=False))

print()
"""

g=pd.DataFrame(np.array([-1,0,2,3,4,6,8,3,9,5,4,7,11,6,12,9]).reshape(4,4),index=list("abcd"),columns=[5,4,3,2])

print(g)

#print(g[[5,3]])
#print(g["a":"c"])
#print(g[1:4])

f=pd.DataFrame(np.array([-1,0,2,3,4,6,8,3,9,5,4,7,11,6,12,9]).reshape(4,4),index=[10,8,6,4],columns=[5,4,3,2])

print("")
print(f)

print("")
print(f.reindex(index=[10,9,8,7,6,5,4],method="ffill"))

print("")


h=pd.Series(["a","b","c","d"],index=[10,8,6,4])

print(h)
print(h.reindex([10,9,8,7,6,5,9.8,4],method="ffill"))

print(h.reindex([10,10.4,8.6,6.999],method="ffill"))

h1=pd.Series([1,2,3,4],index=[10,8,6,4])

print(h1)
print(h1.reindex([1,1.1,2.2,4,4.5],method="ffill"))

