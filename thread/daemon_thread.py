from threading import Thread,current_thread

from time import sleep
def teacher():
	for i in range(1,11):
		print(i)
		sleep(1)

t1=Thread(target=teacher)
mt=current_thread()
print(" mt :" ,mt.isDaemon())
print("t1 ",t1.isDaemon())

t1.setDaemon(True)
print("t1 :",t1.isDaemon())

t1.daemon=False
print("t1 :",t1.daemon)
t1.daemon=True

t1.start()
sleep(6)
print("main thread ")

