# Decorators
# What is decorators?
# A function that takes another function as an argument and returns a new function.
from functools import wraps

def decorator(func):
    def wrapper():
        print("Transection Intitiated")
        func()
        print("Transection Completed")

    return wrapper

@decorator
def transfer():
    print("Money Transfered")


transfer()

