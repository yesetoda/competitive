class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for r in range(row-1,-1,-1):
            for c in range(col-1,-1,-1):
                right = float("inf")
                if c+1<col:
                    right = grid[r][c+1]
                down = float("inf")
                if r+1<row:
                    down = grid[r+1][c]
                val =  min(right,down)
                grid[r][c] += val if val != float("inf") else 0
         
        return grid[0][0]