"""Given two strings, str1 and str2, find the length of the shortest string that has both the input strings as subsequences.

str1 = "yabc"
str2 = "xabc"
There can be multiple strings that have str1 and str2 as subsequences, 
for example, "xyaabcc" and "xyabbc", but the shortest string that has these input strings as subsequences is "xyabc". """


def shortest_common_supersequence(str1, str2):
    rows = len(str1) # str1 - vertical
    cols = len(str2) # str2 - horizontal 
    dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
    max_common = 0
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            if str1[row-1] == str2[col-1]:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row][col-1], dp[row-1][col])
            max_common = max(max_common, dp[row][col])
    l = rows + cols
    l = l - max_common
    return l

"""
Find the longest common subsequence length and then subtract it from the length of the combined string. 
"""

"""
Time Complexity: O(N * M), where N is the length of s1 and M is the length of s2.
Space Complexity: O(N * M), where N is the length of s1 and M is the length of s2.
"""
