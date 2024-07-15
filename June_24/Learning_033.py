# The fliter function in python is a built in function.
# allows you filter elements in a list,tuple,set.

numbers = [1,2,3,4,5,6,7,8,9,10]
def is_even(num):
    return num%2 == 0

new_evn_number = filter(is_even,numbers)
print(list(new_evn_number))

letters = ['a','b','c','d','e','f','g''h','i','j','k','l','m','n','o','p','q']

def find_vowels(letter):
    vowels = ['a','e','i','o','u']
    return letter in vowels

new_vowels = find_vowels('a')
print(new_vowels)

filtered_vowels = filter(find_vowels,letters)
print(list(filtered_vowels))

