# https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        cols = len(triangle[0])
        dp = []
        col = 1
        for row in triangle:
            l = [0] * col
            col += 1
            dp.append(l)
        dp[-1] = triangle[-1]
        col = rows
        for r in range(rows-2, -1, -1):
            for c in range(col-1):
                dp[r][c] = triangle[r][c] + min(dp[r+1][c], dp[r+1][c+1])    
            col -= 1
        return dp[0][0]

"""
Time Complexity: O(N * M), where N is no. of rows and M is no. columns
Space Complexity: O(N * M), where N is no. of rows and M is no. columns
"""
