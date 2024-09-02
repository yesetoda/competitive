class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
        self.rem = n
    def find(self,x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)
        if xrep != yrep:
            if self.size[xrep]>=self.size[yrep]:
                self.parent[yrep] = xrep
                self.size[xrep] += self.size[yrep]
                self.rem-=1
            else:
                self.parent[xrep] = yrep
                self.size[yrep] += self.size[xrep]
                self.rem-=1
        
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for i,j in edges:
            uf.union(i,j)
        counts = Counter(map(uf.find, range(n))).values()
        return sum(map(mul, accumulate(counts, add, initial=0), counts))


        