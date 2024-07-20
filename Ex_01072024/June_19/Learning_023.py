# List
# List of collection

# indexing
my_list = [1, 2, 3, 4, 5]
print("Element at  index 0-",my_list[0])

# changing an  element
my_list[1] = 10
print("list after changing element 1", my_list)

# append
my_list.append(20)
my_list[3] = 90
print("list after appending -",my_list)

# extend
my_list.extend([6,7])
print("list after extending-",my_list)

# Insert function
my_list.insert(4, 'a')
print("list after inserting-", my_list)

#Remove function
my_list.remove('a')
print("list after removing-", my_list)

my_copy_list = my_list.copy()
print("copy of list-", my_copy_list)

my_list.clear()
print("Initial list", my_list)
print("copy of list after clearing-", my_copy_list)

print("Index of 3 in list-", my_list.index(3)) # because my_list is deleted

#Not operator works in boolean true false >>>>>>imp




#