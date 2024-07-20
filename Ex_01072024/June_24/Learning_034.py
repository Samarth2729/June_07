# Map - returns a list of the results after applying the given function
# to each item of a given iterable ( list, tuple etc)
# pick 1 number znd apply a function to it.
# give the same number of elements
#in the output as the input.

numbers = [1,2,3,4,5,6,7,8,9,10]

def square(number):
    return number**2
squared_numbers = map(square,numbers)
print(list(squared_numbers))

# filter - function that return true and false
# pick the item if true return it if false remove it.
# it can give less number of items as compared tpo list.

def is_even(number):
    return number % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))
