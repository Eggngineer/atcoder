from math import sqrt
a,b=map(int,input().split())

c = sqrt(a**2+b**2)
x = a/c
y = b/c
print(x," ",y)