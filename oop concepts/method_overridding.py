# method overridding 

class parent:
	def add(self,a,b):
		print(a+b)
class child(parent):
	# this add method override add method of parent class as their name is same 
	def add(self,a,b,c):
		
		print(a+b+c)
c=child()
c.add(10,20,30)
print("\v\tsuper method ")
print("**********************************")
# super method to call the method of parent class that was overridden 

class parent1:
	def add(self,a,b):
		print(a+b)

class child1(parent1):
	
	def add(self,a,b,c):
			super().add(a,b)
			print(a+b+c)
c1=child1()
c1.add(10,20,30)

		