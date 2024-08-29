class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent =  [i for i in range(len(stones))]
        size = [1]*len(stones)
        ans = 0
        def find(x):
            if x != parent[x]:
                x = find(parent[x])
            return parent[x] 
        def union(x,y):
            nonlocal ans
            xrep = find(x)
            yrep = find(y)
            if xrep == yrep:
                return
            if size[xrep]>=size[yrep]:
                parent[yrep]= xrep
                size[xrep]+=size[yrep]
            else:
                parent[xrep]= yrep
                size[yrep]+=size[xrep]
            ans +=1
        x,y = {},{}
        for ind,(i,j) in enumerate(stones):
            if i in x:
                union(ind,x[i])
            else:
                x[i] = ind
            if j in y:
                union(ind,y[j])
            else:
                y[j] = ind
        
        return ans



        