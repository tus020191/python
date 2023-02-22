# palindrome number and star  pattern 

def palindrome_number_star():
	n=int(input("enter number: "))
	for row in range(1,n+1):
		for col in range(1,((3*n)+2)+1):
			if((col<=(2*n)-1-row) or (col>=(2*n)+row-1)):
				print("* ",end="")
			else:
				if((row%2==0 and col%2==0 ) or(row%2!=0 and col %2!=0)):
					print(row,end=" ")
				else:
					print("* ",end="")
		print("")

palindrome_number_star()		
