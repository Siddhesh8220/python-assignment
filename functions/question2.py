# 2] Write a Python function
# which accepts two arguments x and y and returns (x + y) * (x + y).

# Test
# Data : x
# = 4, y = 3

# Expected
# Output :
# (4 + 3) ^ 2) = 49


x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))

def calculate(x,y):
    return (x+y)*(x+y)

print(calculate(x,y))