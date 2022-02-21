# 2] Write a Python program
# that accepts an integer (n) and computes the value of n+nn+nnn.

# Sample
# value of n is 5

# Expected
# Result : 155

n = int(input("Enter a number: "))
result = n + n*n + n*n*n
print(f"Result is: {result}")