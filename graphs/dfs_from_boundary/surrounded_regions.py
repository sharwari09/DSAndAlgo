# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[False for j in range(cols)] for i in range(rows)]
        for col in range(cols):
            if board[0][col] == "O" and not visited[0][col]:
                self.dfs(board, visited, 0, col, rows, cols)
            if board[rows-1][col] == "O" and not visited[rows-1][col]:
                self.dfs(board, visited, rows-1, col, rows, cols)

        for row in range(rows):
            if board[row][0] == "O" and not visited[row][0]:
                self.dfs(board, visited, row, 0, rows, cols)
            if board[row][cols-1] == "O" and not visited[row][cols-1]:
                self.dfs(board, visited, row, cols-1, rows, cols)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and not visited[row][col]:
                    board[row][col] = "X"


    def dfs(self, board, visited, row, col, rows, cols):
        visited[row][col] = True
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            for d in range(4):
                xrow = r + dx[d]
                ycol = c + dy[d]
                if self.isValid(xrow, ycol, rows, cols) and not visited[xrow][ycol] and board[xrow][ycol] == "O":
                    stack.append((xrow, ycol))
                    visited[xrow][ycol] = True

    def isValid(self, row, col, rows, cols):
        return row >= 0 and row < rows and col >= 0 and col < cols
