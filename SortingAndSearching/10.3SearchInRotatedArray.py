"""
Given a sorted array of n integers, that has been rotated an unknown number of spaces, write code to find an 
element in the array you may assume that the array was originally sorted in increasing order.
Example:
Input: num = 5, arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 6, 10, 14]
Output: 8 (the index)
"""

def binarySearch(num:int, arr:list) -> int:
    """
    Time Complexity: O(log n) where n is the amount of elements in the array
    Space Complexity: O(1)
    """

    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + ((r - l)// 2)
        if num == arr[mid]:
            return mid
        if arr[l] <= arr[mid]:
            if arr[l] <= num < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if arr[mid] < num <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
    
if __name__ == "__main__":
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 6, 10, 14]
    assert binarySearch(5, arr) == 8
    assert binarySearch(8, arr) == -1
    
    arr = [6, 7, 1, 2, 3, 4, 5]
    assert binarySearch(1, arr) == 2
    assert binarySearch(4, arr) == 5
    assert binarySearch(6, arr) == 0

    arr = [3, 1]
    assert binarySearch(1, arr) == 1