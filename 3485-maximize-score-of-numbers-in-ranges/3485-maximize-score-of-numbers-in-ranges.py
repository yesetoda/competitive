class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        def check(val):
            prev = start[0]
            for i in range(1,len(start)):
                cur = prev + val
                if cur <= start[i]:
                    prev = start[i]
                elif cur > start[i]+d:
                    return False
                else:
                    prev = cur
            return True
        l,r = 0, d + start[-1]-start[0]

        while l<r:
            mid = l + (r-l)//2+1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l

