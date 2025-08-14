"""
Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and
s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring. (e.g., "waterbottle" is a 
rotation of "erbottlewat").
"""

def isSubstring(s:str, sub:str) -> bool:
    return sub in s

def stringRotation(s1:str, s2:str) -> bool:
    doubled_string = s1 + s1
    return isSubstring(doubled_string, s2)


if __name__ == "__main__":
    assert stringRotation("erbottlewat", "waterbottle") == True
    assert stringRotation("erbottlewati", "waterbottle") == False
    assert stringRotation("abcde", "cdeab") == True
    assert stringRotation("abcde", "abced") == False
    assert stringRotation("a", "a") == True
    assert stringRotation("a", "b") == False
    assert stringRotation("", "") == True
    assert stringRotation("abc", "") == True
    assert stringRotation("", "abc") == False
    assert stringRotation("rotation", "tionrota") == True
    assert stringRotation("rotation", "ationrot") == True
    assert stringRotation("rotation", "tationro") == True