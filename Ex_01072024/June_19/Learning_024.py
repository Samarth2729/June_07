my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(list)
# temp_list = []
# for i in list:
#     temp_list.append(i*2)
#     print(temp_list)


# Map Function
# takes the each item from the list
# executes the function on each item
# returns the list of results
def double_item(number):
    return number*2
print(list(map(double_item, my_list)))
print(my_list)

