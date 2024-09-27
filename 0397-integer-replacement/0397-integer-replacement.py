class Solution:
    def integerReplacement(self, n: int) -> int:
        dp ={1:0}
        def rec(x):
            if x in dp:
                return dp[x]
            if x%2:
                dp[x] = 1 + min(rec(x-1),rec(x+1)) 
            else:
                dp[x] = 1 + rec(x//2)
            return dp[x]
        return rec(n)