# 1] Write a Python program to
# get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.

str =  input("Enter a string: ")
def newStr(str):
    if str[:2] == "ls":
        return str
    else:
        return "ls"+str

print(newStr(str))