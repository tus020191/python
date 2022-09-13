from threading import Thread
from queue import Queue
from time import sleep

class product:
	def __init__(self):
		self.q=Queue()
	def produce(self):
		for i in range(1,6):
			sleep(2)
			print(f"product {i } is produced")
			sleep(2)
			self.q.put(i)
			
class consumer:
			def __init__(self,p):
				self.p=p
			def consume(self):
				for i in range(1,6):
					print(f"product { self.p.q.get()} ready \n")
				print("end ....... ")

prod=product()
consu=consumer(prod)
t1=Thread(target=prod.produce)
t2=Thread(target=consu.consume)

t2.start()
t1.start()
			