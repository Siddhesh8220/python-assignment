try:
    a = 1/0  
    print (a)
except ArithmeticError:  
    print ("Divide by zero")


try: 
    arr = [3,5,3,4,5,6] 
    print (arr[9]) 
except IndexError: 
    print ("Index Error")


try:
    print(result)
except NameError:
    print("Result not defined")


try:
    from crypt import pwd
except ImportError:
    print("Import not found")

try:
        hello="string"
except IndentationError:
    print("Identation error")