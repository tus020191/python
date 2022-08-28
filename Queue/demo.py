from queue import Queue ,LifoQueue
from collections import deque

class A:
    def __init__(self) -> None:
        self.a=5
    def f(self,b):
        tmp=b
        tmp.a=55
        return tmp
        


def fun(a: list[int])-> None:
    pass

l=[5,7]
k=l.copy()
print(k)

b=A()
c=b.f(b)
c.a=89

print(b.a)

q=Queue(maxsize=6)
d=deque()
q.put(50)
print(q.get())
d.append(45) # right append

d.appendleft(66)# append left
d.appendleft(666)# append left
print(d[0])
print(d[len(d)-1])
print(d[1])
