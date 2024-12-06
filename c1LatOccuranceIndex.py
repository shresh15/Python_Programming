numbers = [12, 32, 55, 67, 3, 55, 68, 22, 55, 89, 55, 1, 19, 32]

li = len(numbers) - 1 - numbers[::-1].index(55)
print(li)

#len(numbers) - 1 - numbers[::-1]

#numbers[::-1] =sequence[start:stop:step]
#: : no value provided so dafault is start and stop of list