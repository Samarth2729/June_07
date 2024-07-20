# Q 1.Difference Btw the = operator and == operator in python.
# Ans-> Basically = operator is used to assign values to the variables.
# And == operator is used to compare two values.
# Example->
name = "Samarth" # Here = operator is used to assign value to the variable.
x = 40
y = 60
print(x if x==y else y) # Here == operator is used to compare two values.

# Q 2.What does the ** operator do in python and how it used ?
# Ans-> So,** operator is used to calculate power of a number.
# Example->
print(2**3) # Here 2 is base and 3 is power.

# Q 3.What does the ^ operator do in python and in what context is it commonly used ?
# Ans-> THe ^ operator is used for the bitwise OR operations.The operator compares the bit
# Example->
x = 30 # binary of 30 is 0011110
y = 40 # binary of 40 is 0100100
#step1
x = x ^ y # x becomes 0011110 and y becomes 0100100 which is 0111010 (binary for 58)
x = 58
#step2
y = x ^ y # using updated valiue of x
y = 58 ^ 40 # x becomes 0111010 and y becomes 0100100 which is 0011110 (binary for 30)
y = 30
#step2
x = x ^ y # using updated value of y
x = 58 ^ 30 # x becomes 0111010 and y becomes 0011110 which is 0100100 (binary for 40)
x = 40
# Now X is 40 and Y is 30



