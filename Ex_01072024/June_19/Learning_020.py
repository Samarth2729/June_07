# Functions scope

def outer_function():
    x = 25
    def inner_function():
        print(x)
    inner_function()


outer_function()

# Collection of items
numbers = [1,2,3]
def type_num(smrths_list):
    smrths_list.append(4)
    smrths_list[1] = 200
    return numbers


l = type_num(numbers)
print(l)
