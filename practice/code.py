
class Sol :

    def issafe(self, row,col,n,m):
        
        return True if( row>=0 and row<n and col >=0 and col<m ) else False 
        
    
    def solveTopDown(self, row, col ,n,m,M, memory):
            
            # diagonally  up right
            if(self.issafe(row-1,col+1,n,m)):
                
                if(memory[row-1][col+1]==-1):
                    
                    memory[row-1][col+1]=self.solveTopDown(row-1,col+1,n,m,M, memory)
                
                
            # diagonally down right
            
            if(self.issafe(row+1,col+1,n,m)):
                
                if(memory[row+1][col+1]==-1):
                    
                    memory[row+1][col+1]=self.solveTopDown(row+1,col+1,n,m,M,memory)
                
                
            
            
            #  right
            
            if(self.issafe(row,col+1,n,m)):
                
                if(memory[row][col+1]==-1):
                
                    memory[row][col+1]=self.solveTopDown(row,col+1,n,m,M,memory)
                
            
            return max(memory[row-1][col+1] ,memory[row+1][col+1],memory[row][col+1]) + M[row][col]
            
            
            
            
            
    def maxGold(self, n, m, M):
            # code here
            
            ans=0
            
            memory= [ [-1 for i in range(m)  ]  for j in range (n) ]
            
            for i in range(n):
                
                ans= max(self.solveTopDown(i,0,n,m,M, memory),ans)
            
            print(ans)

M= [[1, 3, 1, 5],
     [2, 2, 4, 1],
     [5, 0, 2, 3],
     [0, 6, 1, 2]]

obj=Sol()
obj.maxGold(4,4,M)


