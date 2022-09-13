from abc import ABC,abstractmethod
# making abstract class 
# abstract class cannot have object 
# if and only if they had abstract
# method defined 
# abstract class can have concrete method as well
# abstract method must be defined in child class 

# same rule as of normal class inheritance 

# if we define only abstract method then 
# this abstact class become interface 

class father(ABC) :# abstract class 
	def __init__(self,gun):
		self.gn=gun
		#super().__init__()
		
	@abstractmethod  # decorator 
	def  area(self):# abstract nethod 
		print("do something ")
		
	def gun(self): # concrete method 
		print(self.gn)

class child(father):
		def __init__(self,weight,g):
			# override constructor of parent
			# calling constructor of parent class
			super().__init__(g)
			self.weight=weight
		
		# must have defination of abstract method of parent class
		def area(self,ar): # this override the base class area method ,so we can use super method
			#super().area()
			self.ar=ar
			
			
		
		
# cannot be made
#my=father()	
c=child(46,"AKM" )
c.gun()
c.area("air force ")
print(c.ar)

print(c.weight)


