class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=0
        a=0
        for i in nums:
            if i==0:
                c+=1
            else:
                nums[a]=i
                a+=1
      
        for i in range(c):
            nums[a]=0
            a+=1
    