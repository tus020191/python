# basic 

"""
# int data type

a= 5 # int type 

print(type(a))

b= "123"
b= int(b)

print(b, type(b))

c="eri"

# give value error 
# c= int(c) 

d=int("0101", base=2)
print(d)

print(int("123"))

print(5/2)
print(5//2)
print(50/2,type(50/2))

# a and b are the pointers only so they point to the same int object 
# with value 5 
a=5
b=5
print("memory location of a and b same -: ", a is b)

"""
"""

# float type

f1=56.5
f2=56.5

print("memeory of f1 and f2 same - :  ", f1 is f2)

# value error exception 
# f3= float("df")

f4= float("5.6")
f5= 5.6
f6= float("5.6")
print("memeory of f4 and f5 same - :  ", f4 is f5)

print("memeory of f4 and f6 same - :  ", f4 is f6)

print(f4)

print("remainder of f4/3", f4%3 )


"""


# # string

# in place change in string is not possible at all in python ..

s1= "Tushar"
print(s1)

s2=str(45)
print(s2)

s3="45"
s4="45"

print("memory of s3 and s4 same -: ", s4 is s3)

print("memory of s2 and s3 same -: ", s2 is s3)


print("memory of s3 ", hex(id(s3)))

s3= s3+ "45"  # here it will allocate another memory with string 4545

print("memory of s3 after concatination", hex(id(s3)))

s3="".join( [s3, "hello"] )

print("memory of s3 ", s3,hex(id(s3)) )


s4= s3.replace("45", "tushar", 1) # replace only one instance of 45, if not then all replace.

print(s3,s4)



