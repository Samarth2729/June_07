# OS Module
# This module provides a way of using operating system dependent functionality.
import os
# get working directory
print(os.getcwd())
# change directory
os.chdir('C:\\Users\\user\\Desktop\\Python')
# get list of files in the directory
print(os.listdir())
# create a new directory
os.mkdir('new_dir')
# remove a directory
os.rmdir('new_dir')
# create a new file
open('new_file.txt', 'w').close()
# remove a file
os.remove('new_file.txt')
# rename a file
os.rename('old_name.txt', 'new_name.txt')
# get environment variables
print(os.environ.get('PATH'))
# sizes of a file
print(os.path.getsize('new_file.txt'))
#  >>>>>>>>>>>>>>>>>>>>>>>....................
