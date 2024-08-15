# https://leetcode.com/problems/distinct-subsequences/description

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        rows = len(s) # s1 - Vertical
        cols = len(t) # s2 - Horizontal
        dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
        for row in range(rows+1):
            dp[row][0] = 1
        for col in range(1, cols+1):
            dp[0][col] = 0
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                dp[row][col] = dp[row-1][col]
                if s[row-1] == t[col-1]:
                    dp[row][col] += dp[row-1][col-1]
                    
        return dp[rows][cols]


"""
Time Complexity: O(N * M), where N is the length of s1 and M is the length of s2.
Space Complexity: O(N * M), where N is the length of s1 and M is the length of s2.
"""
