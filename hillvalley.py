def hillvalley(a):
	count=0
	valley=0
	hill=0
	for i in range(len(a)-1):
		if(a[i]<a[i+1]):
			if(valley==1):
				count+=1
			hill=1
			valley=0
		else:
			if(hill==1):
				count+=1
			valley=1
			hill=0
	if(count==1):
		return True
	return False

a=[27,25,23,21,19,14]
print("ans=",hillvalley(a))

			
			
		
		
		
		
				
				
				
		
		
		
		
		
		
		
		
	
			
			
		
			
		
		
		
		

ans=hillvalley([1,3,5,7,18,14,13,12,10,9])
print(ans)		
				
			
		