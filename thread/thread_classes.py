from threading import Thread

class my_thread(Thread):
	def __init__(self,a):
		Thread.__init__(self) 
		# or 
		#super().__init__() # calling constructor of Thread module
		self.a=a
	# run method which calls up automatically when thread start
	def run(self):
		print("run method")
		for i in range(1,6):
			print(f"child thread ={self.a}")

## making object of my_thread class
t1=my_thread(1)
t2=my_thread(2)
t1.start()
#t1.join()
t2.start()
#t2.join()
for i in range(1,6):
	print("parent thread ")


	