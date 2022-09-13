

# instance variable  
# defined inside constructor .
# separate copy is created for each instance.

# class /static variable
# one copy is created and each instance share same copy of variable.
# change in value is reflected in each instance.



class mobile:
	def __init__(self,model):
		self.model=model  #instance variable
		
	#self.model="xxxx" # not allowed
	
	def model_name(self): # instance method
		print(self.model)
		self.model="changed" # instance variable can be accessed only inside instance method, if used inside class 
		print(self.model)
		
	# class variable
	fp="yes"  # class variable
	
	
	@classmethod # decorator for class method
	def access_class_var(cls): # class method
		print(cls.fp) # cls is same that of self
		# cls is used for class variables
		
	
		









smg=mobile("samsung")
vivo=mobile("vivo")

smg.model_name()
smg.model='hdd'# accessing instance var outside class

print(smg.model)

print(mobile.fp)# accessing class var outside class 

mobile.access_class_var()
mobile.fp="no" # modifying class var
mobile.access_class_var()# accessing class method 

