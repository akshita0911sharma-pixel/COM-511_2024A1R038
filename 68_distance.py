1. WAP to store two points at tuples and calculate the distance between them.

import math

x1=int(input("Enter the x1 value:"))
x2=int(input("Enter the x2 value:"))
y1=int(input("Enter the y1 value:"))
y2=int(input("Enter the y2 value:"))

t1=(x1,y1)
t2=(x2,y2)

formula=math.sqrt((t2[0]-t1[0])**2+(t2[1]-t1[1])**2) # *0.5
print(formula)
