class Solution:
    def jump(self, nums: List[int]) -> int:
        leng = len(nums)
        ls = [0]*leng
        for i in range(leng-2,-1,-1):
            x = float("inf")
            for j in range(nums[i],0,-1):
                if i+j>=leng-1:
                    x = 0
                    break
                else:
                    x = min(x,ls[i+j])
                    if x == 0:
                        break
            ls[i] = x+1
        return ls[0] 

                
