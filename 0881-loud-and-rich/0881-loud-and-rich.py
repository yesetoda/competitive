class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        leng = len(quiet)
        indeg = [0]*leng
        parent = defaultdict(set)
        for a,b in richer:
            parent[a].add(b)
            indeg[b]+=1
        q = deque()
        for i in range(leng):
            if indeg[i] == 0:
                q.append([i,i])
        ans = [i for i in range(leng)]
        while q:
            cur,ind = q.popleft()
            if quiet[ans[ind]]<quiet[ans[cur]]:
                ans[cur] = ind
            for nbr in parent[cur]:
                indeg[nbr] -= 1
                if quiet[ans[cur]]<quiet[ans[nbr]]:
                    ans[nbr] = ans[cur]
                if indeg[nbr] == 0:
                    q.append([nbr,ans[nbr]])
        
        return ans
                
