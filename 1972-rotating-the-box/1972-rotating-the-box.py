class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        row,col = len(box),len(box[0])
        ans = [deque() for _ in range(col)]
        for i in range(row):
            cnt = 0
            ob = []
            for j in range(col):
                o = box[i][j]
                if o == "#":
                    cnt+=1
                elif o == "*":
                    ob.append((cnt,j))
                    cnt = 0
            if cnt>0:
                ob.append((cnt,col))
            x = ["."]*(col+1)
            for k in range(len(ob)-1,-1,-1):
                a,b = ob[k]
                x[b] = "*"
                x[b-a:b] = ["#"]*a
            x.pop()
            for i in range(col):
                ans[i].appendleft(x[i])
            
        return ans
        
            
