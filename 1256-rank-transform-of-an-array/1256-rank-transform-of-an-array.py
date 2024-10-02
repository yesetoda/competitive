class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        x = sorted(set(arr))
        ans = []
        for i in arr:
            ans.append(bisect_right(x,i))
        return ans