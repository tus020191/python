import numpy as np

"""
print(np.array([1,2,3,4,5]))
print("")
print(np.array([[1,2],[3,4],[5,6]]))
print("")
print(np.zeros(3))
print("")
print(np.zeros((3,3)))
print("")
print(np.diag([3,4,7,8]))
print("")
print(np.diag([1,4]))


a=np.diag([1,3,5,7])
print("diag(a) is",np.diag(a))

print("")
ar1=np.array([[1,2,3],[4,5,6]]) # 2x3
ar1.shape=(3,2) # reshaping it 

print(np.full((2,3),10))# order,value to be filled
"""

"""

b=np.random.randint(1,10,4,size=(2,2)) # 1 is inclusive , 10 is exclusive
print("four no. from 1 to 9 is ",b)
c=np.random.rand(4)
print("four float bw 0 and 1 is ",c)
d=np.random.rand(3,3)
print("2d array(3x3) containing no. bw 0 and 1\n",d)
"""

"""
x=[]
for i in range(1,6):
	x.append(np.random.randint(1,11,3))
print(np.array(x))
"""


"""
    #seed function to fix value of randint()
np.random.seed(1)
z=np.random.randint(1,101,10)
print(z)

"""
"""

       #  RESHAPE() return array  into other dimensions
         
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
print(a.reshape(6,2))
print(a.reshape(4,3))
print(a.reshape(3,-1))
print("value of a not changed",a)

"""



"""      #  creating 2d array by taking input from user

L=[]
for row in range(1,3):
	x=[]
	for col in range(1,3):
		print("enter ","row",row,col,"col element")
		a=int(input("enter :- "))
		x.append(a)
	L.append(x)
	print("")
print(np.array(L))
"""
"""
##slicing in arrays

np.random.seed(111)
a=np.random.randint(1,101,25).reshape(5,5)
print(a)
print(" ")
print(a[:3])
print(" ")
print(a[:3,:3])
print(a[[2,3]])# give 2nd and 3rd index row
print(a[[2,4]])# give 2nd and 4th index row
"""
"""
#conditional selection in array
a=np.arange(1,16)
print(a)
b=a>10 # or a>10 directly # return array of boolean elements depending upon condition.

print(b)
print(a[b])# or a[a>10] # return array of elements depending upon condition.
)
print("")
print(a[a%2==0])
print("")
a[a%2==0]=222
print("")
print(a)
"""
"""
# operations on arrays
a=np.arange(1,5)
b=np.arange(5,9)
print("a",a)
print("")
print("b",b)
print("")
print("a+b\t",a+b)
print("")
print("a-b\t",a-b)
print("")
print("a**b\t",a**b)
print("")
c=a.reshape(2,2)
d=b.reshape(2,2)
print("c",c)
print("")
print("d",d)
print("")
print("c+d\t",c+d)
print("")
print("c*d\t",c*d)# simple multiplication element by element
print("")
print("matrix multiplication") #real matrix multiplication
print(c.dot(d))

"""
"""
# functions of numpy library
a=np.array([10,20,30,40])
b=a.reshape(2,2)
print(a)
print("")
print("sum",a.sum())
print("")
print("max",a.max())
print("")
print("min",np.min(a))
print("")
print("index of min",np.argmin(a))
print("")
print("5 am bw 1 and 2",np.linspace(1,2,5))
print("")
print("cos of elememts of a ",np.cos(a))
print("")
print(b)
print("sum ",b.sum())
print("")
print("min",np.min(b))
print("row wise sum",b.sum(axis=1))
print("clo wise sum",np.sum(b,axis=0))
print("row wise max",b.max(axis=1))
print("col wise min ",b.min(axis=0))
print("")
print("culmative sum",b.cumsum())
print("")
"""
"""
d=np.array([10,20,30,40,60])
c=np.array([10,20,30,20,30,40,50])
np.random.shuffle(d)
print(d)
print("")
print(np.unique(c))
print("")
print(np.unique(c,return_index=True,return_counts=True))
"""

"""
a=np.array([10,20,30,40])
b=np.array([50,60,70,80])
print(np.hstack((a,b)))
print(np.vstack((a,b)))
print(np.where(a==20)) # gives index where condition is satisfied.
print(np.where(a%3==0))
print(np.searchsorted(a,12))

np.intersect1d(a,b) # common elemnets of a and b

np.setdiff1d(a,b) # elements of a differ from b
np.setdiff1d(b,a) # elements of b differ from a .

"""
"""
a=np.random.uniform(5,10,size=5,3)
# uniform function returns array having no.decimal bw 5(inclusive) and 10(exclusive) and size (5,3) matrix
"""
"""
np.set_printoptions(threshold=6,percision=3)
threshold shows specified no. like
   				[1,2,3,,,,,,,,,12,13,14]

percision make decimal upto specified no.
	like .223,.345 etc
"""