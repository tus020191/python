from threading import Thread,Condition
from time import sleep
def product(l):
	
	cv.acquire()
	
	for i in range(1,6):
		l.append(i)
		sleep(1)
		print(f"Item {i}is packed.....")
	cv.notify()
	cv.release()

def consumer(l):
	cv.acquire()
	cv.wait(timeout=3 )
	print("items are packed and can be dispatched")
	cv.release()
	
l=[]
cv=Condition()
t1=Thread(target=product,args=(l,))
t2=Thread(target=consumer,args=(l,))

t1.start()
t2.start()
