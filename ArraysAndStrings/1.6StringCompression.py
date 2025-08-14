"""
Implement a method to perform basic string compression using the counts of repeated characters. For example,
the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string. You can assume the string has only uppercase and lowercase
letters (a-z).

Follow-up: Imagine you have the compressed string a2b1c5a3, turn it into the original string aabcccccaaa.
"""

def stringCompression(s:str) -> str:
    if not s:
        return s
    
    original = len(s)
    ans = []
    L = 0
    for R in range(len(s)):
        if s[R] != s[L]:
            ans.append(f"{s[L]}{R-L}")
            L = R
    ans.append(f"{s[L]}{R+1-L}")
    return "".join(ans) if len(ans) < original else s

def stringCompression2(s:str) -> str:
    ans = []
    L = 0
    R = 0
    
    while R < len(s):
        if s[R].isnumeric():
            num = ""
            while R < len(s) and s[R].isnumeric():
                num += s[R]
                R += 1
            ans.append(s[L] * int(num))
            L = R
        R += 1
    return "".join(ans) if ans else s

if __name__ == "__main__":
    assert stringCompression("aabcccccaaa") == "a2b1c5a3"
    assert stringCompression2("a2b1c5a3") == "aabcccccaaa"

    assert stringCompression("aa") == "a2"
    assert stringCompression2("a2") == "aa"

    assert stringCompression("abab") == "abab"
    assert stringCompression2("abab") == "abab"

    assert stringCompression("") == ""
    assert stringCompression2("") == ""

    assert stringCompression("aabccdeeeeee") == "a2b1c2d1e6"
    assert stringCompression2("a2b1c2d1e6") == "aabccdeeeeee"

    assert stringCompression("zzzzzzzzzz") == "z10"
    assert stringCompression2("z10") == "zzzzzzzzzz"