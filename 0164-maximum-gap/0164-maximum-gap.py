class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0
        for i in range(len(nums)-1):
            mx = max(mx,nums[i+1]-nums[i])
        return mx
