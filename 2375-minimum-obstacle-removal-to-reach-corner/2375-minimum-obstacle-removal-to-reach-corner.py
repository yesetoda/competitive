class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        def inbound(x,y):
            return 0<=x<row and 0<=y<col
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        def spfa(r,c, a,b):
            dist = [[float('inf')]*c for _ in range(r)]
            in_queue = [[False]*c for _ in range(r)]
            dist[a][b] = 0
            queue = deque([(a,b)])
            in_queue[a][b] = True
            while queue:
                x,y = queue.popleft()
                in_queue[x][y] = False
                for ax,ay in moves:
                    nx,ny = x+ax,y+ay
                    if inbound(nx,ny):
                        if dist[x][y] != float('inf') and dist[x][y] + grid[x][y] < dist[nx][ny]:
                            dist[nx][ny] = dist[x][y] + grid[x][y]
                            if not in_queue[nx][ny]:
                                queue.append((nx,ny))
                                in_queue[nx][ny] = True
            return dist[r-1][c-1]
        ans = spfa(row,col,0,0)
        return ans