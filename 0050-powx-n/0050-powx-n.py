from time import sleep
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        op = -1 if n<0 else 1
        n = abs(n)
        while n>0:
            if n&1:
                if op>0:
                    ans *= x
                else:
                    ans /= x
            n>>=1
            x*=x
        return ans


        