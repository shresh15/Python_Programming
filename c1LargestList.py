numbers=[12,32,55,67,3,55,68,22,55,89,55,1,19,32]

nums=list(set(numbers))
nums.sort()
print(nums)
print(nums[-3:])
# This means "start at the third-to-last element and include all elements up to the end of the list."
