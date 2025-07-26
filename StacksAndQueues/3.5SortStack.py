"""
Write a program to sert a stack such taht the smallest items are on the top. You can use an additional
temporary stack, but you may not copy the elements into any other data structure (such as an array). The 
stack supports the following operations: push, pop, peek, isEmpty.
"""

class MinStack:
    def __init__(self):
        self.mstack = []
        self.tempstack = []
    
    def push(self, x:int) -> None:
        if not self.mstack or x <= self.mstack[-1]:
            self.mstack.append(x)
            return
        while self.mstack and x > self.mstack[-1]:
            self.tempstack.append(self.mstack.pop())
        self.mstack.append(x)
        while self.tempstack:
            self.mstack.append(self.tempstack.pop())

    def pop(self) -> int|None:
        if self.mstack:
            return self.mstack.pop()
        return None

    def peek(self) -> int|None:
        if self.mstack:
            return self.mstack[-1]
        return None

    def isEmpty(self) -> bool:
        return len(self.mstack) <= 0
    
if __name__ == "__main__":
    monotonic_stack = MinStack()
    arr = [4, 6, 1 ,3, 2, 5, 7, 9, 10]
    for num in arr:
        monotonic_stack.push(num)
    while not monotonic_stack.isEmpty():
        print(monotonic_stack.pop())