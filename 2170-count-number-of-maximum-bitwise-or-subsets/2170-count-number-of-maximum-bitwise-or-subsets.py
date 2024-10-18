class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        leng = len(nums)
        mx_or = 0
        for i in nums:
            mx_or = mx_or | i
        ans = set()
        def backtrack(path,cor,ind):
            nonlocal mx_or,leng
            if cor == mx_or:
                ans.add(tuple(sorted(path[:])))
            for i in range(ind,leng):
                path.append(nm[i][1])
                prev = cor
                cor = cor | nm[i][0]
                backtrack(path,cor,i+1)
                path.pop()
                cor = prev
        nm = [(nums[i],i) for i in range(leng)]
        backtrack([],0,0)
        return len(ans)

