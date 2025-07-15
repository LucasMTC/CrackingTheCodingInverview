"""
Implement a function to check if a binary tree is balanced. For the purpose of this question, a balanced
tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more 
than one.
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkBalanced(root:Node) -> bool:
    if not root:
        return True
    ans = True
    def findHeight(root:Node) -> int:
        nonlocal ans
        if not root:
            return 0
        left = findHeight(root.left)
        right = findHeight(root.right)
        if abs(left - right) > 1:
            ans = False
        return 1 + max(left, right)
    
    findHeight(root)
    return ans

if __name__ == "__main__":
    root = Node(0, Node(1, Node(2, Node(3, Node(4)))), Node(5, None, Node(6, None, Node(7, None, Node(8)))))
    assert checkBalanced(root) == False

    root = Node(0, Node(1, Node(2, Node(3, Node(4)))), Node(5, None, Node(6, None, Node(7, None, Node(8)))))
    assert checkBalanced(root) == False

    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    assert checkBalanced(root) == True

    root = Node(1, Node(2, Node(4), None), Node(3))
    assert checkBalanced(root) == True

    root = Node(1, Node(2, Node(4, Node(8)), None), Node(3))
    assert checkBalanced(root) == False

    root = Node(1)
    assert checkBalanced(root) == True

    root = None
    assert checkBalanced(root) == True

    root = Node(1, Node(2, Node(3, Node(4))))
    assert checkBalanced(root) == False

    root = Node(1, Node(2, Node(4), None), Node(3, Node(5), Node(6)))
    assert checkBalanced(root) == True


