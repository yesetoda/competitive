class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        leng = len(timePoints)
        mn = float("inf")
        for i in range(leng):
            prev= timePoints[i-1].split(":")
            now = timePoints[i].split(":")
            next = timePoints[(i+1)%leng].split(":")
            prev = int(prev[0])*60+int(prev[1])
            now = int(now[0])*60+int(now[1])
            next = int(next[0])*60+int(next[1])
            dif1 = abs(prev-now)
            dif2 = abs(now-next)
            if dif1>=12*60:
                dif1 = 24*60 - prev + now
            if dif2>=12*60:
                dif2 = 24*60 - next + now
            mn = min(mn,dif1,dif2)
        return mn
            


