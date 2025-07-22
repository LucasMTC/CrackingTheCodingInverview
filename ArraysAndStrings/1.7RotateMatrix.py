"""
Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer,
write a method to rotate the image by 90 degrees. Can you do this in-place?
"""

def rotateMatrix(matrix:list) -> list:
    """
    Time Complexity: O(n^2) where n is the amount of pixels in the square image
    Space Complexity: O(1)
    """
    n = len(matrix)
    r = 0
    c = 0
    while r < len(matrix):
        if r == c:
            saved = r
            c += 1
            continue
        if c < len(matrix):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            c += 1
        else:
            r = saved + 1
            c = r
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix

if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in rotateMatrix(grid):
        print(row)
    grid = [[1, 2], [3, 4]]
    for row in rotateMatrix(grid):
        print(row)
    grid = [[ 1,  2,  3,  4], [ 5,  6,  7,  8], [ 9, 10, 11, 12], [13, 14, 15, 16]]
    for row in rotateMatrix(grid):
        print(row)