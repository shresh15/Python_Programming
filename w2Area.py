import math
a=(int)(input("Enter first: "))
b=(int)(input("Enter second: "))
c=(int)(input("Enter third: "))
s=(a+b+c)/2
ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
#ar_trc=truncate(ar,2)
print(ar)
