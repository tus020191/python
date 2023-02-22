# hollow half pyramid 

def hollow_inverted():
	row=int(input("enter number of rows: "))
	
	for i in range(1,row+1):
		for j in range(1,row+1):
			if(i==1 or j==1  or j==row-(i-1)):
				print("*",end="")
			else:
				print(" ",end="")
		print("")

		
def hollow():
	row=int(input("enter number of rows: "))
	
	for i in range(1,row+1):
		for j in range(1,row+1):
			if(i==row or j==1  or j==i):
				print("* ",end="")
			else:
				print("  ",end="")
		print("")
												
												
hollow_inverted()
print("----------------------------------------------------------")
hollow()
