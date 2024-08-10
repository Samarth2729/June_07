# recursive function to find factorial of a number
# recursion  is a function which calls itself
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# more examples of recursion



