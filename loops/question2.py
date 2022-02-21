# 2] Write a Python program to
# print out a set containing all the colors from color_list_1 which are not present in color_list_2.

# Test
# Data :

# color_list_1 = set(["White",
# "Black", "Red"])

# color_list_2 = set(["Red",
# "Green"])

# Expected
# Output :

# {'Black',
# 'White'}

list=[]

color_list_1 = set(["White","Black", "Red"])
color_list_2 = set(["Red","Green"])

for color in color_list_1:
    if color not in color_list_2:
        list.append(color)

print(list)