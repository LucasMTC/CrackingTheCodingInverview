"""
Given a Binary Tree, design an algorithm which creates a linked list of all the nodes at each depth (eg. if you 
have a tree of depth D, you'll have D linked lists).
"""
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def treeBFS(root:TreeNode) -> list:
    if not root:
        return []
    ans = []
    queue = deque()
    queue.append(root)

    while queue:
        head = None
        for _ in range(len(queue)):
            curr = queue.popleft()
            if not head:
                head = ListNode(curr.val)
                index = head
                ans.append(head)
            else:
                index.next = ListNode(curr.val)
                index = index.next
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return ans

def printLinkedList(arr:list):
    for head in arr:
        curr = head
        linked_list = []
        while curr:
            linked_list.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(linked_list))

if __name__ == "__main__":
    root = TreeNode(27, TreeNode(13, TreeNode(8, TreeNode(3), TreeNode(14)), TreeNode(19, TreeNode(37), TreeNode(20))), TreeNode(42, TreeNode(31, TreeNode(26), TreeNode(16)), TreeNode(5, TreeNode(9), TreeNode(11))))
    printLinkedList(treeBFS(root))



