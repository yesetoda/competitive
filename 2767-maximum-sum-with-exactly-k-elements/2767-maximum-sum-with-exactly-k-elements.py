class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        x = max(nums)
        return ((x+(x+k-1))*k)//2

            
        