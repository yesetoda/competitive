class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l = 0
        leng = r = len(citations)
        while l<=r:
            mid = (l+r)//2
            ind = bisect_left(citations,mid)
            if mid<=leng-ind:
                l = mid + 1
            else:
                r = mid - 1
        return l-1

