# Find the Longest Common Substring between two strings

def lcs_length(s1, s2):
  rows = len(s1) # s1 - Vertical
  cols = len(s2) # s2 - Horizontal
  max_common = 0
  dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
  for row in range(1, rows+1):
    for col in range(1, cols+1):
      if s1[row-1] == s2[col-1]:
        dp[row][col] = dp[row-1][col-1] + 1
      else:
        dp[row][col] = 0
      max_common = max(max_common, dp[row][col])
  return max_common


"""
Map both the strings in a dp matrix. 
If a character if found common between both the strings at dp[i][j]
then perform dp[i][j] = dp[i-1][j-1] + 1. It basically uses the answer from the diagonal cell and adds ont to it. 
dp[i][j] represents the common substring until ith char of string1 and jth char of string2.
"""

"""
Time Complexity: O(N * M), where N is the length of string1 and M is the length of string2
Space Complexity: O(N * M), where N is the length of string1 and M is the length of string2
"""
