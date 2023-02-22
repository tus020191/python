#pattern printing 

def hollow_rect():
	r=int(input("enter number of rows: "))
	c=int(input("enter number of column:  "))
	for row in range(1,r+1):
		for col in range(1,c+1):
			if(row==1 or row==r or col==1 or col== c):
				print("*",end="")
			else:
				print(" ",end="")
		print("")
		
hollow_rect()


