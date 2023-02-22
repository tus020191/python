#number gusseing 

import random
import math

lower=int(input("enter lower bound: "))
upper=int(input("enter upper bound : "))
print("\n")
x=random.randint(lower,upper)
min_guess,count=round(math.log(upper-lower-1,2)),0
print(f"\t you have only {min_guess}  chance to guesse it ")
print("\n")
while(count<min_guess):
	#count+=1
	try:
		guess=int(input("enter number : "))
		count+=1
	except:
		print("opps you have not entered number , re-enter it \n")
		
		continue
#	print("\n")
	if(guess==x):
		print(f"you have gusses it correctly in {count} try  !!!")
		break
	elif(x>guess):
		print("You guess too low!")
	else:
		print("You guess too high! ")

else:
	print(f"\nThe number is:{x} \n\n \t\tbetter luck next time")
	





