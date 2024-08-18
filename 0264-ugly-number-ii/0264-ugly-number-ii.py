class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = set()
        hp  = [1]
        while n>1:
            cur = heappop(hp)
            ans.add(cur)
            for i in [2,3,5]:
                if cur*i not in ans:
                    heappush(hp,i*cur)
                    ans.add(i*cur)
            n-=1
        return heappop(hp)
                
