class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        leng = len(timePoints)
        mn = float("inf")
        for i in range(leng):
            prev= timePoints[i-1].split(":")
            now = timePoints[i].split(":")
            prev = int(prev[0])*60+int(prev[1])
            now = int(now[0])*60+int(now[1])
            dif1 = abs(prev-now)
            if dif1>=12*60:
                dif1 = 24*60 - prev + now
            mn = min(mn,dif1)
        return mn
            


