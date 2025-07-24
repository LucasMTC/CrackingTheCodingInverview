"""
Write a recursive function to multiply two positive integers without using the * operator. You can use
addition, subtraction, and bit shifting, but you should minimize the number of those operations.
"""

# Bit shifting to the left multiplies a number by 2 and bit shifting to the right divides it by 2.

def recursiveMultiplication(num1:int, num2:int) -> int:
    small = min(num1, num2)
    big = max(num1, num2)

    def recursiveHelper(small, big) -> int:
        """
        Time Complexity: O(log n) where n is the smaller number between num1 and num2
        Space Complexity: O(log n) where n is the smaller number between num1 and num2
        """
        if small == 1:
            return big
        if small == 0:
            return 0
        s = small>>1
        half = recursiveHelper(s, big)
        if small % 2 == 0:
            return half + half
        else:
            return half + half + big
    
    return recursiveHelper(small, big)
        
if __name__ == "__main__":
    assert recursiveMultiplication(2, 6) == 12
    assert recursiveMultiplication(3, 8) == 24
    assert recursiveMultiplication(100, 100) == 10000

