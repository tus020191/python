class Solution:
    def swapstringchar(self,sol:str,index:int,i:int) -> str:
        sol=list(sol)
        sol[index],sol[i]=sol[i],sol[index]
        return  "".join(sol)
        
       
        
        
        
    def allpermutation(self,output:list[str],sol:str,index:int,n:int)->None:
        if(index==n-1): # base case 
            if sol not in  output:
                output.append(sol)
               
            return 
        for i in range(index,n):
            sol=self.swapstringchar(sol,index,i)# swapping the characters
            
            self.allpermutation(output,sol,index+1,n)
            
            sol=self.swapstringchar(sol,index,i) # backtracking
            
    def find_permutation(self, S:str) -> list[str]:
        # Code here
        output=[]
        n=len(S)
        
        self.allpermutation(output,S,0,n)
        output.sort()
        return output
        
if __name__=="__main__":
    obj=Solution()
    S="ABC"
    print(obj.find_permutation(S))