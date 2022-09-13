from time import time,ctime,localtime,sleep
from datetime import datetime,date,time as tme,timedelta

c=time()
print("c=",c)
ct=ctime()
print(f"ct={ct}")
lt=localtime()
print(f"lt={lt}")

dt=datetime(year=2022,month=3,day=6)
print(f"dt={dt}")
d=date(2019,12,14)
d1=date(2019,12,15)
print(f"d1>d {d1>d}")
print(f"d={d}")

tm=tme(hour=12,minute=50)
print("tm=",tm)

today=datetime.today()
print(f"today ={today}")
print(today.strftime("%d-%b %y"))

#help(timedelta)
td=timedelta(days=5)
diff=d-td
print(f"diff={d-td}")

print(diff.strftime("-%d-%m"))

## sleep method of time module
"""
for i in range(1,6):
	sleep(5)
	print(f"i={i}")
"""	
### calculating age 
td=date.today()
dob=date(1990,4,11)
age=td.year-dob.year-((td.month,td.day)<(dob.month,dob.day))
print(f"age={age}")
