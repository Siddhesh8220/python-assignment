# 1] Write a decorator
# function_timer that times the execution of any function it is attached to and print the time taken after the function execution ends.
import time

def function_timer(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print(f"Execution Time: {end-start}")
    return wrapper

@function_timer
def hello():
    a = 0
    for i in range(0,100):
        a += (i**100)
        
hello()




