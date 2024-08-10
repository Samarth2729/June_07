import os
import math

print(os.name)
print(os.getcwd())
print(math.pi)

# Change the directory
#os.chdir("")

# os.mkdir("new_dir")
# Read a file , you just want to check it exists or not

size = os.path.getsize("textdata.tst")
print(size)

if size != 0:
    print("File exists")
else:
    print("File does not exist")

# Get file modification time
mod_time = os.path.getmtime("textdata.tst")
print(mod_time) # the input in epoch time format

import  time

local_time = time.localtime(mod_time)
print(local_time)


