# 1] Write a Python program to
# concatenate all elements in a list into a string and return it.

lis = ["a",1,2,"hello"]
listToStr = ' '.join([str(elem) for elem in lis])
print(listToStr)