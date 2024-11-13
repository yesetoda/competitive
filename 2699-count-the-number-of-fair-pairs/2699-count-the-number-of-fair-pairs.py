class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        print(nums)
        for i in range(len(nums)-1):
            a = bisect_left(nums,lower - nums[i],i+1)
            b = bisect_right(nums,upper-nums[i],i+1)
            ans += b-a
        return ans
