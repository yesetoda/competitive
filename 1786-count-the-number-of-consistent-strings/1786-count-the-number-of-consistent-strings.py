class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        allowed = set(allowed)
        for i in words:
            x = set(i)
            notFound = False
            for j in x:
                if not j in allowed:
                    notFound = True
                    break
            if not notFound:
                cnt+=1
        return cnt

