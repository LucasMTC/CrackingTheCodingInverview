"""
Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.
"""

def zeroMatrix(matrix:list) -> list:
    """
    Time Complexity: O((m * n) * (m + n))
    Space Complexity: O(m * n)
    """
    if not matrix or len(matrix[0]) < 1:
        return [[]]
    m = len(matrix)
    n = len(matrix[0])
    zeros = set()
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zeros.add((r, c))
    
    def eraseRC(r, c):
        for i in range(m):
            matrix[i][c] = 0
        for i in range(n):
            matrix[r][i] = 0

    for zero in zeros:
        eraseRC(zero[0], zero[1])
    return matrix

if __name__ == "__main__":
    matrix = [[1, 2], [1, 2]]
    assert zeroMatrix(matrix) == matrix

    matrix = [[5, 7], [8, 9]]
    assert zeroMatrix(matrix) == [[5, 7], [8, 9]]

    matrix = [[0]]
    assert zeroMatrix(matrix) == [[0]]

    matrix = [[1, 2, 3]]
    assert zeroMatrix(matrix) == [[1, 2, 3]]

    matrix = [[1, 0, 3]]
    assert zeroMatrix(matrix) == [[0, 0, 0]]

    matrix = [[1], [0], [3]]
    assert zeroMatrix(matrix) == [[0], [0], [0]]

    matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    assert zeroMatrix(matrix) == [[1, 0, 3], [0, 0, 0], [7, 0, 9]]

    matrix = [[0, 0], [0, 0]]
    assert zeroMatrix(matrix) == [[0, 0], [0, 0]]

    matrix = [[0, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert zeroMatrix(matrix) == [[0, 0, 0], [0, 5, 6], [0, 8, 9]]

