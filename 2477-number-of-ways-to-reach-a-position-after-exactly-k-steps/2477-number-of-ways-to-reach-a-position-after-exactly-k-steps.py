class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        def fact(n,m = 1):
            ans = 1
            while n>m:
                ans *= n
                n -= 1
            return ans
        def comb(n,r):
            return fact(n, n-r) // fact(r)  
        dist = abs(startPos-endPos)
        if dist%2 != k%2 or k<dist:
            return 0
        else:
            return comb(k,(k+dist)//2)%(10**9+7)

