"""
Given a string write a function to check if it is a permutation of a palindrome. A palindrome is a word or
phrase that is the same forwards or backwards. A permutations is a rearrangement of letters. The palindrome
does not need to be limited to just dictionary words. You can ignore casing and non-letter characters.
"""

def palindromePermutation(s:str):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count = {}
    for char in s:
        if char.isalpha():
            count[char.lower()] = count.get(char.lower(), 0) + 1
    
    unique = False
    for char, c in count.items():
        if c % 2 == 0:
            continue
        else:
            if not unique:
                unique = True
            else:
                return False
    return True

if __name__ == "__main__":
    assert palindromePermutation("Tact Coa") == True
    assert palindromePermutation("") == True
    assert palindromePermutation("123") == True
    assert palindromePermutation("tTact Coa") == False
    assert palindromePermutation("aabb") == True
    assert palindromePermutation("abcabc") == True
    assert palindromePermutation("aabbc") == True
    assert palindromePermutation("aabbccdde") == True
    assert palindromePermutation("a") == True
    assert palindromePermutation("aa") == True
    assert palindromePermutation("Aa Bb!") == True
    assert palindromePermutation("A man, a plan, a canal: Panama") == True
    assert palindromePermutation("!!@@") == True
    assert palindromePermutation("abc") == False
    assert palindromePermutation("1a2a1") == True