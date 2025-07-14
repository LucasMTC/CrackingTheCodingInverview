"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a BST
with minimal height.
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binarySearch(arr:list) -> Node:
    if len(arr) < 1:
        return None
    head = Node(arr[len(arr)//2])
    head.left = binarySearch(arr[:len(arr)//2])
    head.right = binarySearch(arr[len(arr)//2 + 1:])
    return head    

def findMaxDepth(head:Node):
    if not head:
        return 0
    return 1 + max(findMaxDepth(head.left), findMaxDepth(head.right))

if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = binarySearch(arr)
    print(findMaxDepth(head))
    
    # Remember that the max depth of a complete tree is equal to log(len(arr))/log(2) rounded up to the nearest int.
    