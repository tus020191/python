# 


def num_pyramid():
	n=int(input("enter number: "))
	for row in range(1,n+1):
		k=row
		for col in range(1,(2*n-1)+1):
			if(col>=n-(row-1) and col<=n+(row-1)):# condition of triangle
				if(k>=row and col<n): # condition
					print(f"{k} ",end="")# of number
					k+=1                        # pattern
				else:
					
					print(f"{k} ",end="")
					k-=1
			else:
				print("  ",end="")
		print("")


		
def num_half_pyramid():
		n=int(input("enter number: "))
		for row in range(1,n+1):
			for col in range(1,n+1):
				 if(col==1 or col==row or row==n):  # condition for number 
				 	print(f"{col} ",end="")
				 else:  # printing space 
				 	print("  ",end="")
			print("")
			
			
def pali_num1():
	n=int(input("enter the number:  "))
	for row in range(1,n+1):
		k=1
		for col in range(1,((2*row)-1)+1):
			if(col<row):  # number series condition 
				 print(k,end="")
				 k+=1
			else:
				 print(k,end="")
				 k-=1
		print("")
				 
				 
def pyramid_pali():
	n=int(input("enter the number:  "))
	for row in range(1,n+1):
		k=1
		for col in range(1,((2*n)-1)+1):
			if(col>=n-(row-1) and col<=n+(row-1)):
				 if(col<n):  # number series condition 
				 	print(k,end=" ")
				 	k+=1
				 else:
				 	print(k,end=" ")
				 	k-=1
			else:
				print(" ",end=" ")
		print("")					 							
				 						

def pali_alphabet_1():
	n=int(input("enter the number:  "))
	for row in range(1,n+1):
		k=65
		for col in range(1,((2*row)-1)+1):
			if(col<row):  # number series condition 
				 print(f"{chr(k)} ",end="")
				 k+=1
			else:
				 print(f"{chr(k)} " ,end="")
				 k-=1
		print("")				 									 						
				 			
		
num_pyramid()
print("------------------------------------------------")
num_half_pyramid()
print("-------------------------------------------------")
pali_num1()
print('----------------------------------------------------')
pyramid_pali()
print("------------------------------------------------------")

pali_alphabet_1()
print("-----------------------------------------------------")

						