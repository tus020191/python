#class student :
	def __init__(self,name,age):
		self.name=name
		self.age=age
	
class user :
	@staticmethod
	def static(obj):
		print(obj.name)
		print(obj.age)
		
	def fun1(self,obj):
		print(obj.name)
		
stu1=student("tushar",19)
user.static(stu1)
us1=user()
us1.fun1(stu1)




