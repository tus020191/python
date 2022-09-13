# multiple inheritance 

class father :
	
	def sf(self):
		print("accessd father  class method")
		
class mother :
	def sm(self):
		print("accessd mother  class method")
		
class son(father,mother) : # multiple inheritance 
	def ss(self):
		print("accessd son  class method")
		
s=son()
s.sf()
s.sm()
s.ss()
print("\v\v")
## constructor calling for multiple inheritance 

class father1:
	def __init__(self):
		print("father constructor")
		super().__init__()
	def sf(self):
		print("accessd father  class method")

class test:
	def __init__(self):
		print("test constructor")
		super().__init__()
	
	def sm(self):
		super().sm()
		print("accessd test  class method")		
						
class mother1:
	def __init__(self):
	#	super.__init__()
		print("mother constructor")
	def sm(self):
		
		print("accessd mother  class method")
	def same():
		print("mother ")
		
class son1(father1,test,mother1) : # multiple inheritance 

	def __init__(self):
		print("son  constructor")
		super().__init__()
		
	def ss(self):
		print("accessd son  class method")
		
	
		

s1=son1()
s1.ss()
		