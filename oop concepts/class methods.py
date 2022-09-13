# class methods

# same copy of classs variable is shared to all objects ,so change will reflect to all objects.

class mobile:
	def __init__(self,model):
		self.model=model
	
	c="yes"  # class variable
	@classmethod  # decorator 
	def class_method(cls): # cls current class , same as self.
		print(cls.c)
	

realme=mobile("7s")
redmy=mobile("8as")
mobile.class_method()
realme.class_method() # using object calling class method 
print(realme.c) 
print(redmy.c)	
	
# if we change class variable value by using class name ,then it reflect to all objects

mobile.c="no"
print(realme.c)
print(redmy.c)


# if we change class variable value using object then it reflect to only for that object only.

realme.c="yes changed for particular object only "
print(realme.c)# change for it only
print(redmy.c) # no change 

				