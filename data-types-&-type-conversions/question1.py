# 1] Write
# a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

# Sample String :
# 'w3resource'

# Expected Result :
# 'w3ce'

# Sample String :
# 'w3'

# Expected Result :
# 'w3w3'

# Sample String : '
# w'

# Expected Result : Empty
# String

str = input("Enter a String:")
if len(str)>1:
    print(str[0:2]+str[-2:])
else:
    print("")