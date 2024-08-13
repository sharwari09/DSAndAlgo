# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for col in range(n):
                if col > 0: 
                    dp[row][col] += dp[row][col-1]
                if row > 0:
                    dp[row][col] += dp[row-1][col]
        return dp[m-1][n-1]

"""
Time Complexity: O(m * n), where m is no. of rows and n in no. of columns
Space Complexity: O(m * n), where m is no. of rows and n in no. of columns
"""
