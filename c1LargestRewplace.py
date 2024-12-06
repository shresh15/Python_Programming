numbers=[12,32,55,67,3,55,68,22,55,89,55,1,19,32]

lar=max(numbers)

ind=numbers.index(lar)
numbers[ind]=1000
print(numbers)