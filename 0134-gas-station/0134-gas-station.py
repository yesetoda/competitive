class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        go = []
        leng= len(gas)
        path = deque()
        for i in range(leng):
            go.append(gas[i]-cost[i])
        l = r = 0
        sm = 0
        while  l>=0:
            if sm>=0:
                path.append(go[r])
                sm+=go[r]
                r+=1
                r%=leng
            else:
                while sm<0:
                    sm -= path.popleft()
                    l+=1

                    if l == leng:
                        l = -1
                        break
            if len(path) == leng and sm>=0:
                break
        return l
        

            
            
                

