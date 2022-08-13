class Smallestmultiple:
    def __init__(self) -> None:
        from queue import Queue
        self.maxcount=1e06
        self.q=Queue()  # its store num in ascending order

    def converttonum(self,string: str)-> int:
        n=len(string)
        num,pow=0,1
        
        for i in range(n-1,-1,-1):
            rem=ord(string[i] ) - ord("0") # converting char to corresponding int 
            num=num+ rem*pow
            pow*=10
        return num

    def divisible(self,num: int ,x:int)-> bool:
        return True if num%X==0 else False

    def findsmallestnum(self,X:int)->int:
        self.q.put("9")
        while(self.maxcount):
            front=self.q.get() # as numbers are strored in ascending order ,so front contain smaller numbers
            
            
            num=self.converttonum(front) # converting to number
            if(self.divisible(num,X)): # if num is divisible then return 
                return num

            s1=front+"0"
            front=front+"9"
            # add in this order only for ascending order
            # as number added 0 is lesser than number added 9
            self.q.put(s1)
            self.q.put(front)
            self.maxcount-=1
        return -1  # if not divisible 

if __name__=="__main__":
    obj=Smallestmultiple()
    n=10
    while(n):
        X=int(input("enter number: "))
        print(obj.findsmallestnum(X) )
        n-=1



            







    