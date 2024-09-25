class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if not w in cur:
                cur[w] = {}
            cur[w]["cnt"] = cur[w].get("cnt",0)+1
            cur = cur[w]
        cur['*'] = ''

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        ans = []
        tr  = Trie()
        for i in words:
            tr.insert(i)
        for i in words:
            x = 0
            rt = tr.root
            for j in i:
                rt = rt[j]
                x+=rt["cnt"]
            ans.append(x)
        return ans
        