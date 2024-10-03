class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn,mx = arrays[0][0],arrays[0][-1]
        dis = 0
        for i in range(1,len(arrays)):
            a = arrays[i]
            dis = max(dis,a[-1]-mn,mx-a[0])
            mx = max(mx,a[-1])
            mn = min(mn,a[0])
        return dis
