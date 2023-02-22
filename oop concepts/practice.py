class employee:
	def __init__(self,name,id,phone_no):
		self.name=name
		self.id=id
		self.phone_no=phone_no
	def salary(self,sal):
		self.salary=sal

class manager(employee):
	def __init__(self,name,id,phone,dep):
		super().__init__(name,id,phone)
		self.department=dep
	def salary(self,sal):
		self.salary=sal
	
	
	
emp=employee("Tushar",103,789)
print(f"name={emp.name}, id={emp.id} ,phone={emp.phone_no}",end=", ")
		
emp.salary(150000)	
print(f"salary={emp.salary}")

mag=manager("hari",111,456,55)

print(f"name={mag.name}, id={mag.id} ,phone={mag.phone_no}, dep={mag.department}")

		