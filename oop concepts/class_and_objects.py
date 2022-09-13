''' CLASSES AND OBJECTS'''
"""
class hello:
	pass
	
h1=hello()
h2=hello()

h1.msg="hello python"
h2.msg="hello oop in python"

print(h1.msg,"\n",h2.msg)
print("")


class car:
	def __init__(self,speed,color):
		self.spd=speed
		self.clr=color
		
		
ford=car(50,'blue')
honda=car(70,"red")


print("********FORD********")
print(f"speed={ford.spd}\ncolor={ford.clr}")

print("")
print("*******honda********")
print(f"speed={honda.spd}\ncolour={honda.clr}")	




class private:
	__name=None
	public=55
	def set(self,name):
		self.__name=name
	def get(self):
		return self.__name
			
p1=private()
p1.set("tyshar")	
print(p1.get())	
print(p1.public)

# inheritance
class polygon:
	def __init__(self,side):
		self.side=side
		print("yes included",side,'***')
		
	def set_width(self,width):
		self.__width=width
	def set_height(self,height):
		self.__height=height
	
	def get_width(self):
		return self.__width
	def get_height(self):
		return self.__height
		
	
poly=polygon(10)
poly.set_width(20)
poly.set_height(10)

print(poly.get_width(),'\n',poly.get_height())
		
class rectangle(polygon):
	def __init__(self,side):
		super().__init__(12)
	
	
	
	def area(self):
		return self.get_width()*self.get_height()
		
			
rect=rectangle(4)
print("area of rectangle is :-")
rect.set_width(30)
rect.set_height(50)
print(f'width is{rect.get_width()}')
print(f"height is{rect.get_height()}")

print(rect.area())

"""

"""
class func:
	def table(self,num):
		for i in range(1,11):
			print(f"{num}x{i}={num*i}")
	def factorial(self,num):
		print(f"factorial of {num} is:- ",end="")
		fact=num
		while(num>1):
			fact=fact*(num-1)
			num-=1
		print(fact)
	
	def fibonnachi(self,terms):
		x,y=0,1
		print(f"fibonnachi series upto {terms} : ",end="")
		while(terms>=1):
			print(x,end=",")
			
			x,y=y,x+y
			terms-=1
		print(".....")
	
	def palindrome_string(self,word):
			rev_str=""
			for i in word:
				rev_str=i+rev_str
			print(f"given string is {word}")
			print(f"reversed string is {rev_str}")
			if(rev_str==word):
				print("yes given string is palindrome")
			else:
				print("no it is not a palindrome string")
			
	def palindrome_num(self,num):
			print(f"given number : {num}")
			n=num
			#print(n)
			rev_num=0
			while(n):
				rem=n%10
				#print(rem)
				n=n//10
				rev_num=(rev_num*10)+rem
				#print(rev_num)
			print(f" reversed number : {rev_num}")
			if(rev_num==num):
				print("yes it is palindrome ")
			else:
				print("no it is not palindrome number")
	
	def leap_year(self,year):
				if(year%400==0):
					print(f"{year} is a leap year")
				elif(year%100==0):
					print(f"{year} is not a leap year")
				elif(year%4==0):
					print(f"{year} is a leap year")
				else:
					print(f"{year} is not a leap year")
		
				
			
			
			
			
			
			
		



fun1=func()
fun1.table(2)
print("")
print("*************************")
print("")
fun1.factorial(6)
print("")
print("******************************")
print("")	
fun1.fibonnachi(10)		
print("")
print("********************************")
print("")	
fun1.palindrome_string('naman')
print("")
print("**************************")	
fun1.palindrome_num(1321)		

print("")
print("*****************************")

fun1.leap_year(2004)

print("")
print("********************************")

"""
class mobile:
	def __init__(self):
		self.model="samsung"
	self.model="changed"



					