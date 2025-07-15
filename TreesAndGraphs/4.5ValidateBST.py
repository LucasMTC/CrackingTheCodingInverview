"""
Implement a function to check if a binary tree is a binary search tree.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validateBST(root, minimum, maximum):
    """
    Time Complexity: O(n)
    Space Complexity: O(log n)
    """
    if not root:
        return True
    if (minimum and root.val > minimum) or (maximum and root.val < maximum):
        return False
    return validateBST(root.left, root.val, maximum) and validateBST(root.right, minimum, root.val)

if __name__ == "__main__":
    root = TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(15)), TreeNode(30, TreeNode(25), TreeNode(35)))
    assert validateBST(root, float("inf"), float("-inf")) == True

    root = TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(25)), TreeNode(30, TreeNode(15), TreeNode(35)))
    assert validateBST(root, float("inf"), float("-inf")) == False
    
    root = None
    assert validateBST(root, float("inf"), float("-inf")) == True