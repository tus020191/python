class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def findsum(self,A: list[int] ,ans:list[int],sol:list[int] ,sum:int,index:int) -> None:
        
        sol1=sol.copy() # becoz in python list is mutable,so on passing
        # in function its value is changes,that why we make
        # a copy so that in a particular recursive call its value is unchanged
        if(sum==0):
            #print(sol1,sum)
            ans.append(sol1)
            return
        
        while(index< len(A) and sum>0):
            sol1.append(A[index])
            #print(sol1)
            self.findsum(A,ans,sol1,sum-A[index],index)
            index+=1
            sol1.pop() # backtracking 
        
    
    def combinationalSum(self,A: list[int], B:int) -> list:
        ans=[]
        sol=[]
        arr=[]
        
        for i in A:
            if(i not in arr ):
                arr.append(i)
                 
        arr.sort()
        self.findsum(arr,ans,sol,B,0)
        return ans

if __name__=="__main__":
    obj=Solution()
    A=[7,2,5,6]
    sum=16
    print(obj.combinationalSum(A,sum))
