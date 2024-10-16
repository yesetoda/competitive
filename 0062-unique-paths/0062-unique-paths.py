class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(x,till = 1):
            ans = 1
            while x>till:
                ans*=x
                x-=1
            return ans
        return factorial( n + m -2 , n -1)//factorial(m-1)
        