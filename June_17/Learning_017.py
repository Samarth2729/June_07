# Functions
# Block of code that can be reuse
# Define
# Call

# Built functions - bultins.py
# Which are created by the python contributor

def sum_number_arrgument_return(a, b):  # arguments
    return a + b


print(sum_number_arrgument_return(2, 3))  # call the function


def numbers_of_sum(a, b, c):
    return a + b + c


print(numbers_of_sum(2, 3, 4))


# *args - unlimited arguments
def args(*numbers):
    print(numbers)
