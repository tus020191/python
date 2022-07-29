from random import shuffle,randint,choice
class password_generator :
    def __init__(self):
        self.pawd=[]
        self.lst=list('!@#$%^&*')

        self.upper_case1=chr(randint(65,90))
        self.upper_case2=chr(randint(65,90))

        self.lower_case1=chr(randint(97,122))
        self.lower_case2 = chr(randint(97, 122))

        self.num1=chr(randint( ord('1'),ord("9")) )
        self.num2 =chr(randint(ord('1'), ord("9")))

        self.special1=choice(self.lst)
        self.special2 = choice(self.lst)

    def password(self):
        self.st= self.upper_case1 + self.upper_case2 + self.lower_case1 + self.lower_case2 + self.num1 + self.num2 + self.special1 + self.special2
        self.pawd=list(self.st )
        shuffle(self.pawd)
        return "".join(self.pawd)

password1 = password_generator()
pwd=password1.password()
print(password1.pawd)
print(pwd)



