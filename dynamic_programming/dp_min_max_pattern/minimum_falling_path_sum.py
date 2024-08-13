# https://leetcode.com/problems/minimum-falling-path-sum

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[1000 for i in range(cols)] for j in range(rows)]
        dp[-1] = matrix[-1]
        for row in range(rows-2, -1,-1):
            for col in range(cols):
                dp[row][col] =  matrix[row][col] + dp[row+1][col]
                if col > 0:
                    dp[row][col] = min(matrix[row][col] + dp[row+1][col-1], dp[row][col])
                if col < cols-1:
                    dp[row][col] = min( matrix[row][col] + dp[row+1][col+1], dp[row][col])
        return min(dp[0])

"""
Intuition: The idea here is to initialize the last row with the same values from the input matrix and then
using these values to calculate the minimum values to reach to the first row. 
"""


"""
Time Complexity: O(N^2), where N is no. of rows and columns.
Space Complexity: O(N^2), where N is no. of rows and columns.
"""
