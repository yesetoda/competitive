class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=0
        a=0
        i = 0
        while i<len(nums):
            if nums[i]==0:
                c+=1
                nums.remove(0)
            else:
                i+=1
      
        for i in range(c):
            nums.append(0)
           
    