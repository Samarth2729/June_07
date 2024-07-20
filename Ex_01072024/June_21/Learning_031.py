# Dictionary function

my_list = {"name": "John", "age": 30, "city": "New York"}
print(my_list)
print(my_list.items())
print(my_list.keys())
print(my_list.values())
print(my_list["name"])
print(my_list.get("name"))
my_list["age"] = 27
print(my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 4}  # in dict duplicate keys not return but value returned
print(my_dict)
print(my_dict['a'])  # if key is duplicate it will return the last value of the key
print(my_dict.get('a'))  # it will return the value of the key


