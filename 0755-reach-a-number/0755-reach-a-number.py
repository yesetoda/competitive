class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        c = -2*target
        part = (1 - 4*c)**0.5
        root1  = (-1 + part)/2
        root2  = (-1 - part)/2
        ans = int(max(root1,root2))
        val = ans*(ans+1)//2
        while val<target or (target-val)%2:
            ans+=1
            val = ans*(ans+1)//2
        return ans
