# 3] Write a Python program to
# test whether a passed letter is a vowel or not.

letter = input("Enter a letter: ")[0]
vowels = ["a","e","i","o","u"]
if letter in vowels:
    print("It is a vowel")
else:
    print("It is not a vowel")