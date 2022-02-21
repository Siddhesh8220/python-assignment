# 2] Write a Python program to
# get the largest number from a list.

lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    element = int(input())
    lst.append(element) 

print(f"Maximum element: {max(lst)}")