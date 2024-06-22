# SET function
# Collections of items
# Ordered and Unordered
# Mutable and Immutable
# No duplicate members

# Define an empty set

list_of_unique_items = {1,2,3,4,3,2,5,5}
print(list_of_unique_items)
print(type(list_of_unique_items))

# Covert list into set
list1 = [45.2,60,45,60,32,32]
set1 = set(list1)
print(set1) # Unordered

# Union Function
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
my_set = set1.union(set2)
print(my_set)

# Intersection Function
my_set = set1.intersection(set2)
print(my_set)
# Difference Function
my_set = set1.difference(set2)
print(my_set)
my_set = set2.difference(set1)
print(my_set)

