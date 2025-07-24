"""
There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a character. Given two strings, write a function to check if they are one edit (or zero edits)
away.
"""

def oneAway(str1:str, str2:str) -> bool:
    """
    Time Complexity: O(n) where n is the max amount of characters between str1 and str2
    Space Complexity: O(n) where n is the max amount of characters between str1 and str2
    """
    if len(str1) == len(str2):
        diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
                if diff > 1:
                    return False
        return True

    else:
        if abs(len(str1) - len(str2)) > 1:
            return False
        
        for i in range(max(len(str1), len(str2))):
            if i == len(str1) or i == len(str2):
                if i == len(str1) and str1[:] == str2[:i]:
                    return True
                elif i == len(str2) and str1[:i] == str2[:]:
                    return True
                else:
                    return False
            elif str1[i] != str2[i]:
                if str1[:i] + str1[i + 1:] == str2 or str2[:i] + str2[i + 1:] == str1:
                    return True
                return False
        return True
        
if __name__ == "__main__":
    assert oneAway("pale", "ple") == True
    assert oneAway("pale", "pales") == True
    assert oneAway("pale", "bale") == True
    assert oneAway("pale", "bake") == False
    assert oneAway("", "as") == False
    assert oneAway("a", "asd") == False