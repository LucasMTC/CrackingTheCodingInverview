"""
Implement an algorithm to determine if a string has all unique characters.

FOLLOW UP: What if you could not use any additional data structures?
"""

def uniqueCharacters(s:str) -> bool:
    """
    Time Complexity: O(n) Where n is each character in the string
    Space Complexity: O(n) Where n is each key in the dict
    """
    count = {}
    for char in s:
        if char in count:
            return False
        else:
            count[char] = 1
    return True

def uniqueCharacters2(s:str) -> bool:
    """
    Time Complexity: O(n^2) Where n is each character in the string
    Space Complexity: O(1)
    """
    for i in range(len(s)):
        for j in range(len(s)):
            if j == i:
                continue
            if s[i] == s[j]:
                return False
    return True

if __name__ == "__main__":
    assert uniqueCharacters("abcd") == True
    assert uniqueCharacters("") == True
    assert uniqueCharacters("aba") == False
    assert uniqueCharacters("abcdA") == True
    assert uniqueCharacters2("abcd") == True
    assert uniqueCharacters2("") == True
    assert uniqueCharacters2("aba") == False
    assert uniqueCharacters2("abcdA") == True