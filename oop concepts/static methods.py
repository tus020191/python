# static methods 

class mobile:
	fp="yss"
	@staticmethod
	def static(r,p):
		mobile.fp="no"
		print(r,p,sep=',')
		
mobile.static(4,12000)
m,n=mobile(),mobile()

m.static(4,12000)
print(m.fp)
m.fp="abcd"
print(m.fp)
print(n.fp)


