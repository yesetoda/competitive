class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple,obstacles))
        dir = ["north","east","south","west"]
        pos ={"north":(0,1),"south":(0,-1),"east":(1,0),"west":(-1,0)}
        r,c,ind = 0,0,0
        ans = 0
        for com in commands:
            if com == -1:
                ind+=1
                ind%=4
            elif com == -2:
                ind -= 1
                if ind<0:
                    ind = 3
            else:
                for _ in range(com):
                    a,b = r+pos[dir[ind]][0],c+pos[dir[ind]][1]
                    if (a,b) in obs:
                        break
                    r,c = a,b
                    ans = max(ans,r**2+c**2)

        return ans
