# File handling
# How to read a text and write into it in python

# function
# open("file name", "mode") -->
# mode
#  r - read
# w - write
# a - append
# r+ - read and write
# b - binary mode

file = open("test.txt", "w")

# Read and write content
# Read a file
#   Reading entire content >>file = open("test.txt", "r")
# content = file.read()
# line = file.readline()
# lines = file.readlines()
# Close the file
file.close()
