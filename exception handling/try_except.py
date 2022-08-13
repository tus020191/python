"""
inside try write code that can produce error

inside except write code for handling error

else clause execute only when no exception occur ,i,e, except block does not  execute

finally block execute always whether except block executed or not

"""

try:
    a = int(input("enter no. -  "))
    b = int(input("enter no. -  "))
    print(a/b)

    print(" no exception occur becoz if exception has "
          "occured then this line will not executed "
          "i,e, point where exception ,occur the control transferred to except block!!! ")
except (ZeroDivisionError,NameError,KeyboardInterrupt,EOFError,ValueError) as obj:
    print(obj)

else:
    print("else: "
          "         i am get executed only when no exception occur")
finally:
    print('finally:'
          'always get executed irrespective of exception')
