
#revise
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sm = sum(nums)
        if sm<p:
            return -1

        target = sum(nums)%p
        if target==0:
            return 0
        
        leng = len(nums)
        mn = leng
        dt = defaultdict(int)
        dt[0] = -1
        nums[0]%=p
        for i in range(1,leng):
            nums[i]+=nums[i-1]
            nums[i]%=p
        for i in range(leng):
            val = (nums[i]-target)%p
            if val in dt:
                mn = min(mn,i-dt[val])
            dt[nums[i]] = i
    
        return mn if mn<leng else -1
            
