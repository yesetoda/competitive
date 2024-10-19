class Solution:
    def rec(self,n):
        if n == 1:
            return [0]
        prev = self.rec(n-1)
        return prev + [1] + ([1-i for i in prev])[::-1]
    def findKthBit(self, n: int, k: int) -> str:
        result = self.rec(n)
        return str(result[k-1])