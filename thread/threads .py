from threading  import Thread,current_thread,Lock,RLock,Semaphore,BoundedSemaphore

## current_thread gives obj of the current running thread
def fun(a,b):
	for i in range(1,6):
		
	     print("child thread ",a,b)
	print(current_thread().getName())


class emp:
	def show(self,a,b):
		for i in range(6):
			print(f"a= { a} ,b= {b} ")
	

class flight:
	def __init__(self,seat):
		self.s=seat
		# creating object of Lock() class
		self.lock=Lock()
		
	def yes_no(self,num):
		self.lock.acquire(blocking =True ,timeout=-1)
		if(self.s>=num):
			print("yes",current_thread().name)
			self.s-=1
		else:
			print("no")
		self.lock.release()
		
class flight1:
	def __init__(self,seat):
		self.s=seat
		# creating object of RLock() class
		self.lock=RLock()
		print(self.lock)
		
	def yes_no(self,num):
		self.lock.acquire(blocking =True ,timeout=-1)
		print(self.lock)
		if(self.s>=num):
			print("yes",current_thread().name)
			self.s-=1
		else:
			print("no")
		self.lock.release()

class flight2:
	def __init__(self,seat):
		self.s=seat
		# creating object of Semaphore() class
		self.lock=Semaphore(5) # bounded semaphore can also be used 
		# allow access to 5 thread at a time
		self.ct=self.lock._value
		print(self.lock)
		print(self.ct)
		
	def yes_no(self,num):
		self.lock.acquire(blocking =True ,timeout=-1)
		print(f"counter value ={self.lock._value}")
		if(self.s>=num):
			print("yes",current_thread().name)
			self.s-=1
		else:
			print("no")
		self.lock.release()


obj1=emp()	

emp().show(10,20)		
				
# making of thread
t1=Thread(target=fun,args=(5,10),name="hello")

t2=Thread(target=obj1.show,args=(10,20))


t1.start()# starting of thread 
t1.join()
t2.start()
t2.join()
for i in range(1,6):
	print("main thread ")
print("name of child thread=",t1.name)
## assigning names
print(current_thread().getName())

print(t1.getName())
t1.setName("jrhdje")
print(t1.name)
#########################
print("*"*60)

ft=flight(1)
rh=Thread(target=ft.yes_no,args=(1,),name="rahul")

sm=Thread(target=ft.yes_no,args=(1,),name="simran")

ft1=flight1(1)
r=Thread(target=ft1.yes_no,args=(1,),name="ram")

k=Thread(target=ft1.yes_no,args=(1,),name="krishna")

#rh.start()
#sm.start()

#rh.join()
#sm.join()
r.start()
k.start()
r.join()
k.join()
print("*"*60)
obj3=flight2(5)
sem1=Thread(target=obj3.yes_no,args=(4,))

sem2=Thread(target=obj3.yes_no,args=(2,))
sem3=Thread(target=obj3.yes_no,args=(3,))
sem4=Thread(target=obj3.yes_no,args=(4,))

sem5=Thread(target=obj3.yes_no,args=(1,))

sem6=Thread(target=obj3.yes_no,args=(1,))

sem7=Thread(target=obj3.yes_no,args=(1,))
sem1.start()
sem2.start()

sem3.start()
sem4.start()

sem5.start()
sem6.start()
sem7.start()

#print("second time main thread ")
