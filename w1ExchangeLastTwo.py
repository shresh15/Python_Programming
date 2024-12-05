n=input("Enter a number : ")
# nls=list(n)
# nls[-1],nls[-2]=nls[-2],nls[-1]
newnum = n[:-2] + n[-1] + n[-2]
print("Number after swapping last two digits:", newnum)

