# generator
def fun(a,b):
    yield a
    yield b

def  show(a,b):
    while(a<=b):
        yield a
        a+=1
a,b=fun(10,20)
print(a)
print(b,"\n\n")


result=fun(30,45)
print(next(result))
print(next(result))
print(type(result))

res=show(10,15)
for data in res:
    print(data)