# https://leetcode.com/problems/longest-common-subsequence

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        rows = len(s1) # s1 - Vertical
        cols = len(s2) # s2 - Horizontal
        max_common = 0
        dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if s1[row-1] == s2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
            max_common = max(max_common, dp[row][col])
        return max_common

"""
(dp) table helps efficiently compute the longest common subsequence by building up solutions to smaller subproblems. 
Each cell in the table represents the length of the LCS for the respective prefixes of s1 and s2.

Example: dp table for longest common subsequence for strings s1 = "ABCBDAB" and s2 = "BDCAB" will look like the following:

  "" B D C A B
"" 0 0 0 0 0 0
A  0 0 0 0 1 1
B  0 1 1 1 1 2
C  0 1 1 2 2 2
B  0 1 1 2 2 3
D  0 1 2 2 2 3
A  0 1 2 2 3 3
B  0 1 2 2 3 4

LCS between "ABCBDAB" and "BDCAB" is len(BDAB) - 4
"""

"""
Time Complexity: O(N * M), where N is the length of s1 and M is the length of s2.
Space Complexity: O(N * M), where N is the length of s1 and M is the length of s2.
"""
