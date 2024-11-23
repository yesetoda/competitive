class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = [(nums[i],i) for i in range(len(nums))]
        x.sort()
        a = 0
        b = len(nums)-1
        while a<b:
            val = x[a][0] + x[b][0]
            if val > target:
                b-=1
            elif val < target:
                a+=1
            else:
                return [x[a][1],x[b][1]]