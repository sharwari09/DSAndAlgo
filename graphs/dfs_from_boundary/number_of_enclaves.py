# https://leetcode.com/problems/number-of-enclaves/description/

class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        total = 0
        visited = [[False for col in range((n))] for row in range((m))]
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and not visited[row][col]:
                    visited[row][col] = True
                    total += self.dfs(row, col, grid, m, n, visited)
        return total

    def dfs(self, row, col, grid, m, n, visited):
        cnt = 0
        onBorder = False
        stack = [(row, col)]
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        while stack:
            r, c = stack.pop()
            cnt += 1
            if self.onBorder(r, c, grid, m, n):
                onBorder = True
            for k in range(len(dx)):
                xrow = r + dx[k]
                ycol = c + dy[k]
                if self.isValid(xrow, ycol, grid, m, n) and not visited[xrow][ycol] and grid[xrow][ycol] == 1:
                    visited[xrow][ycol] = True
                    stack.append((xrow, ycol))
        if onBorder:
            return 0
        else:
            return cnt
            
    def onBorder(self, row, col, grid, m, n):
        return row == 0 or row== m-1 or col == 0 or col == n-1

    def isValid(self, row, col, grid, m, n):
        return row >=0 and row < m and col >= 0 and col < n

"""
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""
