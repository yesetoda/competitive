
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def add(self, x):
        if x not in self.parent:
            self.rank[x] = 1
            self.parent[x] = x
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            if self.rank[parentX] < self.rank[parentY]:
                self.parent[parentX] = parentY
            elif self.rank[parentY] < self.rank[parentX]:
                self.parent[parentY] = parentX
            else:
                self.parent[parentX] = parentY
                self.rank[parentY] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dt = defaultdict(list)
        for i,j,t in meetings:
            dt[t].append((i,j))
        meetAt = sorted(dt.items())
        secret_holders = set([0,firstPerson])
        

        
        for t,meet in meetAt:
            uf = UnionFind()
            for i,j in meet:
                uf.add(i)
                uf.add(j)
                uf.union(i,j)
                
            grouping = defaultdict(set)
            for p in uf.parent:
                grouping[uf.find(p)].add(p)
            for gp in grouping.values():
                if secret_holders.intersection(gp) != set():
                    secret_holders.update(gp)
        return list(secret_holders)
