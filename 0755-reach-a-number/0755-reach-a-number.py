class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        a = 1
        b = 1
        c = -2*target
        ans1  = -b + (b**2 - 4*a*c)**(0.5)/(2*a)
        ans2  = -b - (b**2 - 4*a*c)**(0.5)/(2*a)
        ans = int(max(ans1,ans2))
        val = ans*(ans+1)//2
        while val<target or (target-val)%2:
            ans+=1
            val = ans*(ans+1)//2
        return ans
