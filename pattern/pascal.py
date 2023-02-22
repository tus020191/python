# pascal's  triangle

def pascal_triangle():
	n=int(input("enter number: "))
	k=1
	r=1
	while(True):
		for col in range(1,r+1):
			if(k<=n):
				print(f"{k} ",end="")
				k+=1		
			else:
				break;#	
		print("")
		r+=1
		if(k>n):	break
		
pascal_triangle()		
	
	