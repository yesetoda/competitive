class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a,b,c in times:
            graph[a].append((b,c))
        def dijkstra(n,graph, start_node):
            time_elapsed = defaultdict(lambda:float("inf"))
            time_elapsed[start_node] = 0
            processed = set()
            heap = [(0,start_node)]
            while heap:
                time,cur = heappop(heap)
                if cur  in processed:
                    continue
                time_elapsed[cur] = min(time_elapsed[cur],time)
                processed.add(cur)
                for n,t in graph[cur]:
                    nt = t + time
                    if nt < time_elapsed[n] and n not in processed:
                        heappush(heap,(nt,n))


            return time_elapsed
        x = dijkstra(n,graph,k)
        ans = -1
        for i in range(1,n+1):
            ans = max(x[i],ans)
        if ans == float("inf"):
            return -1
        return ans

                    