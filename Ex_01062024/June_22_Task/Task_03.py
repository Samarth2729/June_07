# ✅ Anagrams
# String s1 = "silent";
#
# String s2 = "listen";
# namo - mano - onam
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase

def are_anagrams(s1, s2):
    """
    Check if two strings are anagrams of each other.
    """
    # Convert strings to lowercase and sort their characters
    sorted_s1 = sorted(s1.lower())
    sorted_s2 = sorted(s2.lower())

    # Check if the sorted strings are equal
    return sorted_s1 == sorted_s2

# Example usage
string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))