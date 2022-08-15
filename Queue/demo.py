class A:
    def __init__(self) -> None:
        self.a=5
    def f(self,b):
        tmp=b
        tmp.a=55
        #return tmp
        


def fun(a: list[int])-> None:
    pass

l=[5,7]
k=l.copy()
print(k)

b=A()
b.f(b)
print(b.a)


