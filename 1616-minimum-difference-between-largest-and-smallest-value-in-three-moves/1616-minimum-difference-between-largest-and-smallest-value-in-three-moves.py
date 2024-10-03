class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        leng = len(nums)
        mem = {}
        def solve(start,end,cnt):
            if (cnt,start,end) not in mem:
                if cnt == 3:
                    if start<end:
                        return nums[end] - nums[start]
                    else:
                        return 0
                if start>end:
                    mem[(cnt,start,end)] = 0
                    return  mem[(cnt,start,end)]
                else:
                    mem[(cnt,start,end)] = min(solve(start+1,end,cnt+1),solve(start,end-1,cnt+1))
            return mem[(cnt,start,end)]
        return solve(0,leng-1,0)
