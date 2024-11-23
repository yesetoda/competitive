class Solution:
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        r,c = len(board),len(board[0])
        def inbound(i,j):
            return 0<=i<r and 0<=j<c
        def nbr_info(i,j):
            nbr = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
            info ={0:0,1:0}
            for a,b in nbr:
                x,y = i+a,j+b
                if inbound(x,y):
                    info[op[x][y]] += 1
            return info

        op = deepcopy(board)
        for i in range(r):
            for j in range(c):
                information = nbr_info(i,j)
                if information[1]<2:
                    board[i][j] = 0
                elif information[1]==3:
                    board[i][j] = 1
                elif information[1]>3:
                    board[i][j] = 0


        