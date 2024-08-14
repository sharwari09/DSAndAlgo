# Minimum Number of Deletions and Insertions
"""
Given two strings, str1, and str2, find the minimum number of deletions and insertions required to transform str1 into str2.
str1 = "passport"
str2 = "ppsspt"
deletions = 3
insertions = 1
"""

def min_del_ins(str1, str2):
    deletions = 0
    insertions = 0
    rows = len(str1) # str1 - vertical
    cols = len(str2) # str2 - horizontal

    dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
    max_common = 0
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            if str1[row-1] == str2[col-1]:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
            max_common = max(max_common, dp[row][col])
    deletions = rows - max_common
    insertions = cols - max_common
    return [deletions, insertions] 


"""
Time Complexity: O(N * M), where N is the length of s1 and M is the length of s2.
Space Complexity: O(N * M), where N is the length of s1 and M is the length of s2.
"""
