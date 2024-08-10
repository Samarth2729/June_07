import os

for root, dirs, files in os.walk("/Ex_01072024/July_05"):
    print(root, dirs, files)
    print(len(files))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

fd = os.open("testdata.txt", os.O_RDWR)
os.write(fd, b"Hello World")
os.close(fd)

