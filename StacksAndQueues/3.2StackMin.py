"""
How would you design a stack which, in addition to push and pop, has a function min() which returns
the minimum element? push(), pop() and min() should all operate in O(1) time complexity.
"""

class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
            return

        self.stack.append((x, min(self.stack[-1][1], x)))

    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
    
if __name__ == "__main__":
    stack = MinStack()
    print(stack)
    stack.push(-2)
    print(stack.stack)
    stack.push(0)
    print(stack.stack)
    stack.push(-3)
    print(stack.stack)
    print(stack.getMin())
    print(stack.stack)
    stack.pop()
    print(stack.stack)
    stack.pop()
    print(stack.stack)
    print(stack.getMin())
    print(stack.stack)