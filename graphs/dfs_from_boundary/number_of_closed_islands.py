# https://leetcode.com/problems/number-of-closed-islands/

class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for col in range(cols)] for row in range(rows)]
        cnt = 0
        for row in range(0, rows):
            for col in range(0, cols):
                if not visited[row][col] and grid[row][col] == 0:
                    if self.dfs(row, col, visited, grid, rows, cols):
                        cnt += 1
        return cnt
        
    def dfs(self, row, col, visited, grid, rows, cols):
        stack = [(row, col)]
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        close_island = True
        while stack:
            row, col = stack.pop()
            if row in [rows-1, 0] or col in [cols-1, 0]:
                close_island = False
            for d in range(len(dx)):
                xrow = row + dx[d]
                ycol = col + dy[d]
                if self.isValid(xrow, ycol, rows, cols) and grid[xrow][ycol] == 0 and not visited[xrow][ycol]:  
                    stack.append((xrow, ycol))
                    visited[xrow][ycol] = True
        return close_island
        
    def isValid(self, row, col, rows, cols):
        return row < rows and row >= 0 and col < cols and col >= 0

"""
Time Complexity: O(N * M), where N is no. of rows and M is no. of columns.
Space Complexity: O(N * M), where N is no. of rows and M is no. of columns.
"""
