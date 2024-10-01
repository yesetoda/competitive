class Solution:
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        q = deque([click])
        moves = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        r,c = len(board),len(board[0])
        def inbound(x,y):
            return 0 <= x < r and 0 <= y < c
        seen = set()
        while q:
            ln = len(q)
            for i in range(ln):
                x,y = q.popleft()
                if not (x,y) in seen:
                    seen.add((x,y))
                    if board[x][y] == "M":
                        board[x][y] = "X"
                        return board
                    else:
                        mines = 0
                        next = []
                        for a,b in moves:
                            nx,ny = x+a,y+b
                            if inbound(nx,ny):
                                if not (nx,ny) in seen :
                                    if board[nx][ny] == "M":
                                        mines+=1
                                    else:
                                        next.append([nx,ny])
                        if mines == 0:
                            board[x][y] = "B"
                            if next:
                                q.extend(next)
                        else:
                            board[x][y] = str(mines)
        return board
        


                        



