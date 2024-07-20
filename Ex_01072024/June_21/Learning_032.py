my_dist = {'b': 1, 'w': 2, 'c': 3, 'a': 4}
for k,v in  my_dist.items():
    if k == 'b':
        print("Key with the name b is found")

op = 'b' in my_dist
print(op)

