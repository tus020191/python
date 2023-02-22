from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import filedialog as fd
a=Tk()

from tkinter import scrolledtext
a.geometry("4x10")


"""" BIND METHOD
widigit_name.bind(action,function)

action=[<Button>,<Button-1>,<Button-2>,<Button-3>,<Enter>,<any keyboard key>,<Shift-Up> any other combination,<ButtonRelease>,<Motion><>Leave]

button1 for left click
button 2 for wheel 
button 3 for right click


function must be parametrised
lambda function must have arbitary variable when used with bind.

"""





""" config method
used to alter arguments of widigit at any later stage of program
widigit_name.config(arguments )

"""


"""		*****grid*****
grid(row=row,column=column,padx=,pady=,sticky=([W,N,S,E])#make content to stick to particular corner of cell),rowspan=,columnspan=,)

*rowspan make row longer ,i,e merges row
"""

"""	********pack()******

side=LEFT,RIGHT,BOTTOM,TOP
anchor=N,S,W,E,NE,NE,SW,SE
padx=leave space on x dir both side
pady
expand=True,False
fill=BOTH,X,Y,fill the widigit if window grow.

"""

"""*******place()*******
x=x
y=y
width=
height=
"""


"""*******common arguments******

width
height
bd=borderwidth
bg=background colour
fg=foreground colour
relief=(RIDGE,SUNKEN,GROOVE,RIDGE)
font=("type",size,(bold,italic,underline))
state=disabled,normal,readonly

"""


#*******label*******
# using grid
"""
l1=Label(a,text="programming python",bg="red",fg="blue",font=("Gotham",6),width=25,bd=15,relief=RIDGE)


l1.grid(row=0,column=0,sticky=W,padx=104,pady=15,rowspan=3)

l2=Label(a,text="hello",bd=15,relief=RIDGE)
l2.grid(row=3,column=0)

"""
# using pack
"""
l3=Label(a,text="hi")
l3.pack(side=LEFT,padx=5,pady=7,anchor=S)
"""

"""



#****entry*******
var1=StringVar() # IntVar(),
e1=Entry(a,bd=15,relief=GROOVE,state="normal",textvariable=var1)
e1.pack(pady=60)

#e1.insert( index, value to be)
#e1.insert(0,"hi")
#e1.insert(1,"ho1")
#e1.insert(END,"PYTHON")

#e1.delete(startingindex,ending index )
# ending index is exclusive
#e1.delete(1,4)

#var1.get() to store data of entry 
# var1.set(to set value in entry field)
#var1.set("hi how are you")

e1.bind("<Enter>",lambda e: a.configure(bg="blue"))

"""


"""
#********button********
def s1():
	b1.config(bg="red",state="disabled")
	b2.config(state="disabled",bg="red4")

b1=Button(a,text="click",command=s1)
b1.pack(pady=60)
b1.config(bg="yellow")

b2=Button(a,text="clll",command=s1)

b2.pack()
# to call parametrised function use lambda0

def s2(n):
	
	if(n%2==0):
		b1.config(text="yes")
	else:
		b2.config(text="pro")
		
b3=Button(a,text="test",command=lambda: s2(14))
b3.pack()

b4= Button(a,text="python",command=lambda:print("hello world"))
b4.pack()



"""

"""
#******Frame******

# if frame is (pack or grid) then its size automatically expand as widigit are added to it .

# in case of place not increased


# we can add widigit in frame

f1=Frame(a,bd=25,relief=RAISED,bg="firebrick4",width=300,height=90)
f1.pack(side=TOP,pady=100)


"""

"""
# ******Label frame******
# same as frame 
# diff is that it has named frame
lf1=LabelFrame(a,text="food frame",bd=25,relief=RIDGE,width=400,height=500)

lf1.pack()
"""


"""
#******checkbutton******

# default onvalue and offvalue is 1 and 0 respectively
var2=IntVar()
c1=Checkbutton(a,text="python",onvalue=1,offvalue=0,relief=RIDGE,bd=15,variabler=var2,command=)

c1.pack()

c.select() # by default tick
c.deselect()# not tick
var2.get()# if checked then onvalue otherwise offvalue

#command function is called when it is clicked

"""

"""
#*****spinbox******
# command arg. can also be used in spinbox
var3=StringVar()
s1=Spinbox(a,values=["red","blue","green"],textvariable=var3,bd=15,state='readonly',width=50)

s1.pack(pady=150)

#var3.get() # current value
#var3.set("hello")

"""

"""


# ****** Radiobutton*****
# command can be used 

#Radiobutton(a,text,variable,value,command)
var4=IntVar()
r1=Radiobutton(a,value=1,text="rd1",variable=var4)
r1.pack()

r2=Radiobutton(a,value=2,text="rd2",variable=var4)
r2.pack()

var4.get() # give value of that radiobutton which is checked

"""


"""

# combobox
# command can be used 
var5=StringVar()
cb=ttk.Combobox(a,width=30,textvariable=var5,values=("red","blue","green"),state="readonly")

cb.pack(pady=100)

var5.get()# give current value
cb.current(1)# default value give index from 0 to len(values)-1

"""

"""

# message box
#msg.showinfo("title","message to be displayed")

#msg.showwarning("title","message")

#msg.showerror("title","message")

#ans=msg.askyesnocancel("title","message")
# ans hold True if yes pressed ,False if no otherwise None

"""

"""

# text box 
txt=Text(a,width=30,height=20)
txt.pack(pady=150)
#txt.insert(lineno.index,text )
#txt.insert(1.0,"hello world how are\n")
#txt.insert(2.0,"python")
#txt.insert(2.7,"java")

#txt.get(1.0,END)# give all data 
#txt.get(start,end)

#txt.delete(1.0,END)

"""
"""
to save a file 
#file dialog 
file=fd.asksaveasfile(mode="w",defaultextension=".txt")
file.write("hello tkinter ")
file.close()
"""

"""

# notebook
#n1=Notebook(a)
#n1.place
#n1.add(frame,text="")
#n1.bind("<<NotebookTabChanged>>",function)

#n1.index("current") give index of tab which is opend.
"""


a.mainloop()