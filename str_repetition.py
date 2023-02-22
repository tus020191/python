s=input("")

def repfree(s):
  
    lst=list(s)

    l=[]
    for i in lst:
      if(i not in l):
        l.append(i)
        
      else:
        return False
    else:
      return True 
    

print(repfree(s))   





