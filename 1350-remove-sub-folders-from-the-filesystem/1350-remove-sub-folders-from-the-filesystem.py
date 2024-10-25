class Trie:
    def __init__(self):
        self.child = {}
        self.ans = []
    def add(self,s):
        cur = self.child
        for i in s:
            if "*" in cur:
                break
            if not i in cur:
                cur[i] = {}
            cur = cur[i]
        cur["*"] = {}
        for i in cur:
            cur[i] = {}
    def dfs(self,cur,path):
        for i in cur:
            if i == "*":
                self.ans.append(path[:])
                break
            path.append(i)
            self.dfs(cur[i],path)
            path.pop()

        
        
    

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        tr = Trie()
        for i in folder:
            tr.add(i.split("/"))
        tr.dfs(tr.child,[])
        return ['/'.join(i) for i in tr.ans]
        