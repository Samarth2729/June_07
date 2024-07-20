hero1 = ("SpiderMan","Hulk","IronMan")
hero2 = ("Thor", "Hawkeye", "Black Widow")
new_tuple = (hero1,hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[1][2])
print(new_tuple[0][1])

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Unpacking >> assigning different variable
q, w, e = (45,56,78)
print(q)
print(w)
print(e)
t = (4,56,78)
# t.append(100) this willnot work bcs  tuple is immutable
new_t = t + (100, 200, 300)
print(new_t)


# Search in Tuple
cities = ("London", "Paris", "New York", "Tokyo")
print("New York" in cities)
print("New York" not in cities)