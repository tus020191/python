from collections import deque , OrderedDict

from queue import Queue, LifoQueue


"""
#                       ******  SET *******  

s=set() # s={2,4,5}

s.add(67)
s.add(627)
s.add(21)
s.add(4)
s.add(15)
print(s)

# no duplicate 
s.add(5)
print(s)

try :
    s.remove(6)  # key error if not found 

except(KeyError) as obj:

    print("key " ,obj ," not found")


key_in_sorted= sorted(s) # list of elements in sorted order..

print(key_in_sorted)

# iterating the set

# s[2] now possible as the set is not indexed 

# checking 
print(3 in s)


"""

"""

#            ****** dictionary ******


mp= dict() # or mp= {1:2, 3:5}

mp[4]="tushar"
mp[2]="Gupta"
print(mp)

# update the  value of key  4 
mp[4]= "Hello python"
print(mp)

mp[8]="gngd"
print(mp)

try :

    print(mp[6])  # raise key error if the given key is not found . 

except(KeyError) as obj:

    print(obj, "not found ")


print("keys :- ", end="")
for key in mp:

    print(key, end=",")

print()

key= mp.pop(3,"Not Found")  # raise the error if the key is not found or gives the message specified
print(key)

try:

    key=mp.pop(1) # raise the keyerror as no default msg is given 

except (KeyError) as obj:

    print(obj, "Not Found ")


# return the keys
print(mp.keys(), type(mp.keys()))

# return the values 
print(mp.values(), type(mp.values()))

# return the key: value pair as a tuple 
print(mp.items(), type(mp.items))


"""

"""

#       ******** Deque *************

dq=deque()

# append at the last .
dq.append(45)
dq.append(415)
dq.append(453)

print(dq)

# append to the first position 
dq.appendleft(545)
dq.appendleft(245)
dq.appendleft(4135)


print(dq, type(dq))

# pop at last 
dq.pop()

print(dq)

# pop the front 

dq.popleft()
print(dq)

# iteration 

for ele in dq:

    print(ele, end=",")

print()


try:
    dq.index(3) # raise the value error in case of value is not found 

except (ValueError) as obj:

    print()

"""

"""
# ************ Queue ***************


class QueueFull(Exception):

    def __str__(self):
       return "Queue is Full Now"




qu=Queue(5) # size is restricted to 5 , if not given then infinite


# if block =True then wait atmost timeout sec. then raise the error 

# if the block= False then raise the error immediately .  

# qu.get(block=False,timeout=6)


qu.put(56)
qu.put(56)
qu.put(56)
qu.put(56)
qu.put(56)
print(qu.get())  # return and remove the front 

qu.put_nowait(1) # it does not wait for free slot 
# qu.put_nowait(34)
try:

    # gives error as the queue is full now
    if(qu.full()):

        raise QueueFull
    else:
        qu.put_nowait(1) 


except (QueueFull)  as obj:

    print(455555,obj)


** same with LifoQueue

"""



"""

#           ***** Ordered dict  *******

# same functioning that of dict.
orddict= OrderedDict()  # rember the order 

"""

