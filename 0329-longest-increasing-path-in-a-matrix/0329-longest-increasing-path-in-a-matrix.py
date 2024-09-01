class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row,col = len(matrix),len(matrix[0])
        moves = [(0,1),(0,-1),(-1,0),(1,0)]
        def inbound(x,y):
            return 0<=x<row and 0<=y<col
        mem = {}
        def find(x,y,mx):
            if not (x,y) in mem:
                mem[(x,y)] = 1
                for i,j in moves:
                    nx,ny = x+i,y+j
                    if inbound(nx,ny):
                        if mx<matrix[nx][ny]:
                            mem[(x,y)] = max( mem[(x,y)],1 + find(nx,ny,matrix[nx][ny]))
            return mem[(x,y)]

        ans = 0
        for i in range(row):
            for j in range(col):
                x = find(i,j,matrix[i][j])
                ans = max(ans,x)
        return ans

