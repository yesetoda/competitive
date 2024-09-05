class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        mleng = len(rolls)
        msum = sum(rolls)
        x = mean*(n+mleng) - msum
        result = []
        found = False
        # print(x)
        ans = [0]*6
        rem = x
        for i in range(6,0,-1):
            val = i
            cnt = 0
            while rem-val>=n-1 and n>0:
                # print(rem,val,cnt,n)
                rem-=val 
                n-=1
                cnt+=1
            # print(f"{val,rem,n,cnt = }")
            if n == 0:
                ans[val-1] = cnt
                break
            ans[val-1] = cnt
        # print(ans)
        for i in range(6):
            if ans[i]:
                result.extend([i+1]*ans[i])
        if sum(result)<x:
            return []
        return result

