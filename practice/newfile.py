from string import *
"""
def prime():
	a=int(input("enter no"))
	b=a//2
	for i in range(2,b+1):
		if(a%i==0):
			print("not prime")
			break
	else:
		print(" is prime")
for i in range(1,15):
	prime()
	
"""
'''

def arms():
	a=input("enter no")
	l=len(a)
	s=0
	for i in a:
		s=s+(int(i)**l)
		print(s)
	if(s==int(a)):
		print("yes")
	else:
		print("no")
arms()	'''

"""		
def reverse_triangle_shape():
	a=0
	r=int(input("enter rows-: "))
#	c=int(input("enter col"))
	for row in range(r,0,-1):
		for space in range(a):
				if(a<=r-1):
					print(" ",end="")
		a+=1
		for col in range(row):
			print("*",end=" ")
		print(" ")
for i in range(1,6):	
	reverse_triangle_shape()
"""

"""
def t_shape():
	a=int(input("enter rows:- "))
	for row in range(1,a+1):
		if(row==1):
			for i in range(1,a+1):
				print("*",end="")
			print("")
		else:
			for space in range(1,int(a/2)+1):
				print("",end=" ")
			for col in range(1,2):
				print("*")
t_shape()
"""	
	
"""	
def valid():# only containing letters 
#	from string import *
	a=input("enter valid string only:-")
	for i in a:
		if(i  in ascii_lowercase or i in ascii_uppercase):
				pass
		else:
				print("not valid")
				break
	else:
		print("valid")
					
valid()
valid()
"""
"""
def a_shape():
	r=int(input("enter no of rows:- "))
	a=r-1
	b=int((r+1)/2)
	c=1
	d=r
	for i in range(1,r+1):
		for space_1 in range(a):
			print("",end=" ")
		a-=1
		if(i<=b):  # for upper part of A above line of A
			if(i==1):
				print("*")
				print("")
			elif(i!=b):
				print("*",end="")
				for j in range(c):
					print("",end=" ")
				print("*")
				print("")
				c+=2
			else:
				print(r*"*")
		else: # for below part 
				print("*",end="")
				for space_2 in range(d):
					print("",end=" ")
				print("*")
				print("")
				d+=2
					

"""
"""

def strong_no():
			a=input("enter a no. :- ")
			n=0
			def fact(c):
				if(c==1 or c==0):
					return 1
				else:
					return c*fact(c-1)
			for i in range(len(a)):
				n=n+fact(int(a[i]))
			if(n==int(a)):
				print("yes ",a,"is a strong number")
			else:
				print("no",a,"is not a strong number")

strong_no()

				
"""
x=0
y=1
print(x,y,end=",",sep=",")
n=8
while(n):
	 z=x+y
	 print(z,end=",")
	 x=y
	 y=z
	 n-=1

print("")
	 
		
def one():
	def two():
		three()
	
	def three():
		print("yes")
	two()
one()
			   		    	
			   		    
			   		    
			   	
			   
		
		 							
		 							
								
			
	
	