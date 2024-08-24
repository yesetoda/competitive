class Solution:
    def findNthDigit(self, n: int) -> int:
        # ans = [0,9]
        # for i in range(1,10):
        #     ans.append(ans[-1] + (10**i)*(9)*(i+1))
        # print(ans)
        ans = [0, 9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889, 98888888889]
        ind = bisect_left(ans,n)
        val = n - ans[ ind - 1 ]
        x = 10 ** ( ind - 1 ) - 1  
        nm = val // ind
        rem = val % ind
        theval = x + nm
        if rem == 0:
            return int(str(theval)[-1])
        else:
            theval+=1
            rem -=1
            return int(str(theval)[rem])
