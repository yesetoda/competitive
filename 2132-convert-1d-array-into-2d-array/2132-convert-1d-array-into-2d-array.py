class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        leng = len(original)
        if n*m <leng or n*m >leng:
            return ans
        for i in range(m):
            x = []
            for j in range(n):
                x.append(original[i*n+j])
            ans.append(x)
        return ans
