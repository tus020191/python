"""   formatting strings  """

#right justify 
# here * used to show remaining spaces
a="hi{0:*>15} how are {1:*>8}!".format('tushar','you')
print(a)


# left justify 
b="\n\nhi{0:$<15} how are {1:?<10}!".format("tushar","you")

print(b)

#centre justify

c="\n\nhi{:*^15} how are {:*^10}!".format("tushar","youth")
print(c)

#here .xf denote the no of decimal point
d="\n\nhi{: .1f} how are {:*<10d}!".format(3.10,24)

print(d)

"""printing reduced length of parameter"""

#  here .x denote length of parameter
e="\n\nhi{:>4.3} how are {:^.1} {:3d}!".format("tushar","youth",3456789)

print(e)