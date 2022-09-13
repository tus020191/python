from threading import Thread ,Event
from time import sleep
def lt_on():
	# set the internal flag true 
	e.set()
	
	print("Green light on :")
	sleep(4)
	print("stop red light on :")
	e.clear()
	
def traffic():
	e.wait()
	while(e.is_set()):
		print("you may go !!!")
		sleep(1)
	print("done !!!")
	
e=Event()
t1=Thread(target=lt_on)
t2=Thread(target=traffic)

t1.start()
t2.start()	
	
