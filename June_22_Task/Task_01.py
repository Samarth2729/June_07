#✅Right Triangle Star Pattern

n = 5

for i in range(1, n+1):
    print("* " * i)
    print("\n")

# revere traingle star pattern
for i in range(n - 1, 0, -1):
    print('*' * i)

# Palindrome string

def is_palindrome(word):
    word = word.lower()

    reversed_word = word[::-1]

    if word == reversed_word:
        return True
    else:
        return False


print(is_palindrome("delivered"))

