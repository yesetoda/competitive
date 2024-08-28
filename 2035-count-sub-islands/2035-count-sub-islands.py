class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid2)
        col = len(grid2[0])
        seen = set()

        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(x,y):
            return 0<=x<row and 0<=y<col

        cnt = 0
        for i in range(row):
            for j in range(col):
                if not (i,j) in seen and grid2[i][j] == 1:
                    inc = True
                    if grid1[i][j] == 0:
                        inc= False
                    q = deque([(i,j)])                  
                    while q:
                        ln = len(q)
                        for _ in range(ln):
                            x,y = q.popleft()
                            for nx,ny in moves:
                                nx+=x
                                ny+=y
                                if inbound(nx,ny) and not (nx,ny) in seen:
                                    if  grid2[nx][ny] == 1:
                                        if  grid1[nx][ny] == 0:
                                            inc = False
                                        q.append((nx,ny))
                                        seen.add((nx,ny))
                    cnt+= inc
        return cnt
                




