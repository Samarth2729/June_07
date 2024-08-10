# ✅ String Reverse
# 3-4 ways to do this in Python

def reverse_str(string):

    reversed_string = string[::-1]

    return reversed_string


print(reverse_str("Hello"))

# ✅ Count vowels and consonants in a String

def count_vowels_and_consonants(string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = 0
    consonant_count = 0

    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count

print(count_vowels_and_consonants("hello World"))












