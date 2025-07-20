"""
Implement a MyQueue class which implements a queue using two stacks.
"""

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x) -> None:
        """
        Time Complexity: O(n)
        Space Complextiy: O(n)
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        self.stack2.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def deque(self) -> None:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.stack1.pop()
    
    def peek(self) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return self.stack1[-1]

    def size(self) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return len(self.stack1)
    
if __name__ == "__main__":
    queue = MyQueue()
    for i in range(1, 5):
        queue.enqueue(i)
    
    print(queue.size())

    print(queue.peek())
    queue.deque()
    print(queue.peek())
    queue.deque()
    print(queue.peek())
    queue.deque()
    print(queue.peek())