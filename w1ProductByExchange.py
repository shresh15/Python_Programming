n1=input("enter first number: ")
n2=input("enter first number: ")
new_n1=n1[:-1]+n2[-1]
new_n2=n2[:-1]+n1[-1]
ans=(int)(new_n1)*(int)(new_n2)
print(ans)