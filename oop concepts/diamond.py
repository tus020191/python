from abc import ABC
class a():
	def __init__(self,**kw3):
		print("yes")
		
		self.name=kw3['name']
		print(kw3)
		
		
class b(a):
	def __init__(self,**kw2):
		self.age=kw2['age']
		super().__init__(**kw2)

class c(a):
	def __init__(self,**kw1):
		self.car=kw1["car"]
		super().__init__(**kw1)
		
		
class d(c,b):
	def __init__(self,**kw):
		self.rank=kw["rank"]
		super().__init__(**kw)
		

c1=c(car="mercedes",name='tushar')
d1=d(rank=101,car="bugatti",age=21,name="Tushar Gupta")
print("*"*60,'object d')
print(d1.car,d1.name,d1.rank,d1.age,sep="\n")

print(d.__mro__)
print("*"*60 ,"object c")
print(c1.car, c1.name)

