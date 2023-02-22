class stu():
	def __init__(self,fname,lname):
		self.f=fname
		self.l=lname
	def fullname(self):
	    return self.f+" "+self.l
	def id(self):
		return self.f+self.l+'@gmail.com'
"""a=stu('tushar','gupta')
print(a.f)
b=a.fullname()
c=a.id()
print('full name',b)
print('id',c)
"""
a=stu(fname="tushar,",lname="gupta")
print(a.f)



		