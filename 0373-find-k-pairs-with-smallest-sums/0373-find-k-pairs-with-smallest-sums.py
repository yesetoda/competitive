class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hp = [[i+nums2[0],0,i] for i in nums1]
        heapify(hp)
        leng = len(nums2)
        # print([1]*10000)
        ans = []
        for i in range(k):
            sm,ind,nm1 = heappop(hp)
            ans.append([nm1,nums2[ind]])
            if ind+1<leng:
                heappush(hp,[nm1+ nums2[ind+1],ind+1,nm1])
        return ans
        