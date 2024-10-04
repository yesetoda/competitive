class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        prof_dif = list(zip(difficulty,profit))
        prof = 0
        prof_dif.sort(key= lambda x:(x[0],-x[1]))
        leng = len(prof_dif)
        prof_dif[0]  = list(prof_dif[0])
        for i in range(1,leng):
            prof_dif[i] = [prof_dif[i][0],max(prof_dif[i-1][1],prof_dif[i][1])]
        for i in worker:
            ind = bisect_left(prof_dif,[i,0])
            if ind == len(prof_dif):
                ind = -1
            if prof_dif[ind][0]>i:
                ind-=1
                if ind == -1:
                    continue
            prof+=prof_dif[ind][1]
        return prof
            
            
        