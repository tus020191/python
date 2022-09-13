# nested class 

class army:   # outer class
	def __init__(self,name,gun_name):
		self.name=name
		# gun is object of inner class Gun
		self.gun=self.Gun(gun_name) 
	class Gun:   # inner class 
		def __init__(self,name):
			self.capacity="75 rounds"
			self.name=name
			

a=army("Tushar","AK47")
print(a.gun.capacity)
# or 
g=a.gun # assigning name to object 
print(g.name)
# or 
g1=army("aditi","DHDH").Gun("DHDH")
print(g1.name))
		
		
	





