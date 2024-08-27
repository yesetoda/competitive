class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        q = deque([[1,start_node]])
        nbr = defaultdict(set)
        ind = 0
        for i,j in edges:
            nbr[i].add((j,succProb[ind]))
            nbr[j].add((i,succProb[ind]))
            ind+=1
        ans = 0
        seen = set()
        ls = [0]*n
        while q:
            leng = len(q)
            for _ in range(leng):
                success,node = q.popleft()
                ls[node] = max(ls[node],success)
                seen.add(node)
                for i in nbr[node]:
                    val = max(success*i[1],ls[i[0]])
                    if i[0] == end_node:
                        ans = max(val,ans)
                    if (i,val) not  in seen:
                        if val>0:
                            q.append([val,i[0]])
                            seen.add((i,val))
        return ans
                    

