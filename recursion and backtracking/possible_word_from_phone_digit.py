class Solution:
    def matrix(self)-> list:
        dict_no=[" "," ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        return dict_no
        
    def combination(self,a:list[int],output:list[int],word:str,dict_no:list[str],current_index:int,n:int)->None:
        """
        for a particular recursive call index value remain same 
        and we iterate the string stored for that index 
        for eg if index=2 and for 2 string is "abc"
        so we iterate through abc keeping index=2
        """
        if(current_index==n):
            output.append(word)
            return
        
        for i in dict_no[a[current_index]]:
            word+=i
            self.combination(a,output,word,dict_no,current_index+1,n)
            word=word[:len(word)-1] # backtrack 
            
            
        
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a:list,N:int)-> list:
        #Your code here
        dict_no=self.matrix()
        output=[]
        self.combination(a,output,"",dict_no,0,N)
        
        return output


if __name__=="__main__":
    obj=Solution()
    a=[2,3,4]
    n=3
    
    print(obj.possibleWords(a,n))


