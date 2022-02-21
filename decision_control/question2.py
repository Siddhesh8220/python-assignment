# 2] Write a Python program to
# find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

num = int(input("Enter a numer: "))
if(num % 2 == 0):
    print(f"{num} is an even number")
else:
    print(f"{num} is a odd number")