class UnionFind:
    def __init__(self,x,y):
        self.area = 0
        self.parent = []
        self.size = []
        for i in range(x):
            a,b = [],[]
            for j in range(y):
                a.append((i,j))
                b.append(1)

            self.parent.append(a)
            self.size.append(b)
    def find(self,x,y):
        while (x,y) != self.parent[x][y]:
            a,b = self.parent[x][y]
            self.parent[x][y] = self.parent[a][b]
            x,y = self.parent[x][y]
        return (x,y)
    def union(self,x,y,a,b):
        x1,y1 = self.find(x,y)
        x2,y2 = self.find(a,b)
        if (x1,y1) != (x2,y2):
            if self.size[x1][y1] >= self.size[x2][y2]:
                self.parent[x2][y2] = (x1,y1) 
                self.size[x1][y1] += self.size[x2][y2]
                self.area = max(self.area,self.size[x1][y1])
            else:
                self.parent[x1][y1] = (x2,y2)
                self.size[x2][y2] += self.size[x1][y1]
                self.area = max(self.area,self.size[x2][y2])
            
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        x,y = len(grid),len(grid[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        def inbound(a,b):
            return 0<=a<x and 0<= b< y

        uf  = UnionFind(x,y)
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    uf.area = max(1,uf.area)
                    for ax,ay in moves:
                        nx,ny = i+ax,j+ay
                        if inbound(nx,ny) and grid[nx][ny] == 1:
                            uf.union(i,j,nx,ny)
        return uf.area
                        

        
