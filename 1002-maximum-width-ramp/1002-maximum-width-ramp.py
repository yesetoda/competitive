class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ind = sorted([i for i in range(len(nums))],key = lambda x:(nums[x]))
        mx_width,mn_ind = 0,float("inf") 
        for i in ind:
            mx_width,mn_ind = max(mx_width,i-mn_ind) , min(mn_ind,i)
            if mx_width == len(nums):
                break
        return mx_width

