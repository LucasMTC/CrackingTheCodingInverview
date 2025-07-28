"""
You are given two sorted arrays, A and B, where A has a large enough bufffer at the end to hold B.
Write a method to merge B into A in sorted order.
"""

def sortedMerge(a:list, b:list, countA:int, countB:int) -> list:
    n = countA + countB - 1
    pa = countA - 1
    pb = countB - 1
    
    if not b:
        return a
    
    while n >= 0:
        if pa >= 0 and a[pa] > b[pb]:
            a[n] = a[pa]
            pa -= 1
        else:
            a[n] = b[pb]
            pb -= 1
            if pb < 0:
                b[pb] = float("-inf")
        n -= 1
    return a




if __name__ == "__main__":
    A = [2, 4, 6, 7, None, None, None]
    B = [1, 3, 5]
    assert sortedMerge(A, B, 4, len(B)) == [1, 2, 3, 4, 5, 6, 7]

    A = [1, 2, 3]
    B = []
    assert sortedMerge(A, B, 3, 0) == [1, 2, 3]

    A = [None, None, None]
    B = [1, 2, 3]
    assert sortedMerge(A, B, 0, 3) == [1, 2, 3]

    A = [5, 6, 7, None, None, None]
    B = [1, 2, 3]
    assert sortedMerge(A, B, 3, 3) == [1, 2, 3, 5, 6, 7]

    A = [1, 2, 3, None, None, None]
    B = [4, 5, 6]
    assert sortedMerge(A, B, 3, 3) == [1, 2, 3, 4, 5, 6]

    A = [2, 4, 4, None, None, None]
    B = [4, 4, 5]
    assert sortedMerge(A, B, 3, 3) == [2, 4, 4, 4, 4, 5]

    A = [3, None]
    B = [2]
    assert sortedMerge(A, B, 1, 1) == [2, 3]

    A = [1, 3, 5, None, None, None]
    B = [2, 4, 6]
    assert sortedMerge(A, B, 3, 3) == [1, 2, 3, 4, 5, 6]

    A = [5, None]
    B = [5]
    assert sortedMerge(A, B, 1, 1) == [5, 5]

    A = [0, 2, 4, None, None, None]
    B = [-3, -1, 1]
    assert sortedMerge(A, B, 3, 3) == [-3, -1, 0, 1, 2, 4]
