class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float("inf")]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for i,j,k in edges:
            dist[i][j] = dist[j][i] = k
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    dist[j][k] = min(dist[j][k],dist[j][i]+dist[i][k])
        ans = [[i,0] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if dist[i][j]<= distanceThreshold:
                    ans[i][1]+=1
        ans.sort(key= lambda x:(x[1],-x[0]))
        return ans[0][0]
