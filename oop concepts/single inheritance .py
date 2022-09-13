#  single inheritance 

class father():
	def __init__(self): # constructor
		print("called father class constructor")
	def f1(self,money):
		print(money)
		
		
class son(father):   # inheriting father class
	# also inherit constructor of father class
	
	def show(self,r):  
		print(r)
		
s=son()
s.f1(500000)
s.show("bmw")




print(f"**************\n\n")

##### constructor overriding ####



class parent():
	def __init__(self): # constructor
		print("called father class constructor")
	def f1(self,money):
		print(money)
		
		
class child(parent):   # inheriting father class
	# child  constructor  override constructor of father class
	def __init__(self):
		print("child constructor override father constructor ")
		
	def show(self,r):  
		print(r)		


c=child()

print("*******************************\n\n")

###### super method for calling father constructor along with child constructor 

class parent1():
	def __init__(self,m): # constructor
		print("called father class constructor")
		print(m)
		
	def f1(self,money):
		print(money)
		
		
class son1(parent1):   # inheriting father class
	# also inherit constructor of father class
	def __init__(self,x,m):
		super().__init__(m)
		print("")
		print("child class constructor is also called")
		print(x)
		
		
	def show(self,r):  
		print(r)

s1=son1(50,1000)		