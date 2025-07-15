"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a BST
with minimal height.
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minimalTree(arr:list) -> Node:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(arr) < 1:
        return None
    mid = len(arr)//2
    head = Node(arr[mid])
    head.left = minimalTree(arr[:mid])
    head.right = minimalTree(arr[mid + 1:])
    return head    

def findMaxDepth(head:Node):
    if not head:
        return 0
    return 1 + max(findMaxDepth(head.left), findMaxDepth(head.right))

if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert findMaxDepth(minimalTree(arr)) == 4
    
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert findMaxDepth(minimalTree(arr)) == 4

    arr = [0, 2, 3]
    assert findMaxDepth(minimalTree(arr)) == 2

    arr = []
    assert findMaxDepth(minimalTree(arr)) == 0
    # Remember that the max depth of a complete tree is equal to log(len(arr))/log(2) rounded up to the nearest int.
    