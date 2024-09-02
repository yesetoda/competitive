class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        leng = len(chalk)
        chalk = list(accumulate(chalk))
        ind = 0
        mx= chalk[-1]
        if mx<k:
            k -= (k//mx)*mx
        ind = bisect_right(chalk,k)
        if ind <leng:
            return ind%leng
        k-=chalk[-1]
        return ind%leng
        

