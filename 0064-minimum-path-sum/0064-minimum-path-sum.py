class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for i in range(col-2,-1,-1):
            grid[-1][i] += grid[-1][i+1]
        for r in range(row-2,-1,-1):
            for c in range(col-1,-1,-1):
                right = float("inf")
                if c+1<col:
                    right = grid[r][c+1]
                down = float("inf")
                if r+1<row:
                    down = grid[r+1][c]
                grid[r][c] += min(right,down)
         
        return grid[0][0]