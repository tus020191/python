from tkinter import *


#********main window****#

a=Tk()
a.title("practice")
a.resizable(0,0)# (True,False),(0,1),(1,0)
a.geometry("400x400")

a.config(bg="red4")

#*************widigits***************#

"""		
******common arguments******

bg=background colour
fg=foreground  colour
width
height
bd=border width
relief=styles to border(RIDGE,GROOVE,SUNKEN,RAISED)

font=(type,size,(bold,italic,underline))

"""
 
			
"""
***********LABEL**************   

    
Label(where to add,text=,bg,fg,bd,relief,font=(style,size,(bold or italic ,underline)),width,height)  
 """

Label(a,text="hello world",bg="blue",fg="pink",width=50,bd=5,relief= RIDGE)






































a.mainloop()