# hollow full pyramid 

def hollow_pyramid():
	print("")
	print("")
	
	row=int(input("enter number of rows : "))
	print("")
	print("")
	
	for i in range(1,row+1):
		for col in range(1,((2*row)-1)+1):
			if(i==row or col ==row-(i-1) or col==row+(i-1)):
				print(" *",end="")
			else:
				print("  ",end="")
		print("")
		


def hollow_inverted_pyramid():
	print("")
	print("")
	
	row=int(input("enter number of rows : "))
	print("")
	print("")
	
	for i in range(row,0,-1):
		for col in range(1,((2*row)-1)+1):
			if(i==row or col ==row-(i-1) or col==row+(i-1)):
				print(" *",end="")
			else:
				print("  ",end="")
		print("")		
				
		
hollow_pyramid()

hollow_inverted_pyramid()