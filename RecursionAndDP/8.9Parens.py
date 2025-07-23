"""
Implement an algorithm to print all valid (i.e properly opened and closed) combinations of n pairs of parenthesis.
"""

def generateParenthesis(n:int) -> list:
    ans = []
    curr = []

    def backtracking(curr, ans, leftN, rightN):
        if leftN == rightN == n:
            ans.append("".join(curr))
            return

        if leftN < n:
            curr.append("(")
            backtracking(curr, ans, leftN + 1, rightN)
            curr.pop()
        
        if rightN < n and rightN < leftN:
            curr.append(")")
            backtracking(curr, ans, leftN, rightN + 1)
            curr.pop()

    backtracking(curr, ans, 0, 0)
    return ans

if __name__ == "__main__":
    assert generateParenthesis(1) == ['()']
    assert generateParenthesis(2) == ['(())', '()()']
    assert generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]