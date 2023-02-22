# diamond 

def diamond():
	n=int(input("enter number :")) # rows number
	k=(n+1)//2
	#row=coloumn
	for row in range(1,n+1):
		for col in range(1,n+1):
			if(col<=k-row or col<=row-k or col>k):
				print(" ",end="")
			else:
				print("* ",end="")
		print("")



def half_diamond():
	n=int(input("enter number :")) # column number
	
	#row=coloumn*2-1
	for row in range(1,((2*n)-1)+1):
		for col in range(1,n+1):
			if((col<=row and n>=row) or(col<=(2*n)-row and row>n) ):
				print("* ",end="")
			else:
				print(" ",end="")
		print("")

		
def hollow_diamond():
		n=int(input("enter number "))
		# row=column=2n-1
		for row in range(1,(2*n-1)+1):
			for col in range(1,(2*n-1)+1):
				if((col==n-(row-1)or (col==n+(row-1)) and row<=n)or (((col==row-(n)+1) or col==3*n-(row+1)) and row>n) ):
					print("*",end="")
				else:
					print(" ",end="")
			print("")			
		
diamond()

half_diamond()
hollow_diamond()