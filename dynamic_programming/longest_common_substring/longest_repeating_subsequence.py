# https://www.geeksforgeeks.org/longest-repeating-subsequence/#

def find_LRS(str):
    rows = cols = len(str) 
    max_common = 0
    dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            if (str[row-1] == str[col-1]) and row != col:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
    return dp[-1][-1]

"""
(dp) table helps efficiently compute the longest common subsequence by building up solutions to smaller subproblems. 
Each cell in the table represents the length of the LCS for the respective prefixes of s1 and s2.
This problem is similar to finding longest common subsequence but the only constraint is to check if the indices are different before
using the value from the diagonal cell.
"""

"""
Time Complexity: O(N^2), where N is the length of s1.
Space Complexity: O(N^2), where N is the length of s1.
"""
