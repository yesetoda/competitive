class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        leng= len(gas)
        path = deque()
        l = r = 0
        sm = 0
        while  l>=0:
            if sm>=0:
                val = gas[r]-cost[r]
                path.append(val)
                sm+=val
                r = (r + 1) % leng
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
        

            
            
                

