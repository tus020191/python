class myexception(Exception):
   pass
money=10000
withdraw=float(input("enter :  "))
balance=money-withdraw
try:
    if(balance <= 2000):
        raise myexception ("insufficient balance ")
    print(balance)
except myexception as obj:
    print(obj)



