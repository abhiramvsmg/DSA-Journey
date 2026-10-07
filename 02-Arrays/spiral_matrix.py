class Solution:
    def spiralOrder(self, matrix):

        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Left → Right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Top → Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Right → Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
solution = Solution()

print(solution.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

print(solution.spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]))