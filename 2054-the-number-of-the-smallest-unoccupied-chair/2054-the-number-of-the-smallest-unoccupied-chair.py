class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        hp = list(range(10**4))
        heapify(hp)
        ra = [[] for i in range(10**5+10)]
        target_time = times[targetFriend][0]
        times.sort()
        points = set()
        for i in range(len(times)):
            s,e = times[i]
            ra[s].append(s)
            ra[e].append(-s)
            points.add(s)
            points.add(e)
       
        for i in sorted(points):
            if i>target_time:
                break
            for j in sorted(ra[i]):
                if j <0:
                    heappush(hp,ra[-j][0])
                else:
                    ra[j] = [heappop(hp)]
       
        if len(ra[target_time]) != 1:
            ra[target_time] = [heappop(hp)]
        return ra[target_time][0]





