# Break-> based on condition it will break the loop
# Continue-> based on condition it will skip that iteration

# Pass-> it will do nothing > skip the code
for i in range(10):
    if i == 5 or i == 6:
        pass
    else:
        print(i)

# and & or ----
for i in range(1,10):
    if i % 4 == 0:
        print(i) 
    else:
        print(i*2)
