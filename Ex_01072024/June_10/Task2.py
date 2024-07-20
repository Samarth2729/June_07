# 1 Q->Develop a python script that calculates the square and cube of a given number. num=2
num = 2
print(num ** 2)
print(num ** 3)
# 2 Q-> Create a programm that takes two number as input and print whether the first number is greater than,
# less than or equal to the second number.
num1 = int(input("Enter first number:\n "))
num2 = int(input("Enter second number:\n "))
print(num1 if num1>num2 else num2)
print(num1 if num1<num2 else num2)
print(num1 if num1==num2 else num2)