class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        leng = len(intervals)
        ls = [[i,intervals[i]] for i in range(leng)]
        ls.sort(key=lambda x:x[1])
        inds,vals = [],[]
        for i,j in ls:
            inds.append(i)
            vals.append(j)
        ans = [-1]*leng
        for i in range(leng):
            ind = bisect_left(vals,[vals[i][1],-10**(6)])
            if ind<leng:
                ans[inds[i]] = inds[ind]
        return ans
