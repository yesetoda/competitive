class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        st = set(allowed)
        cnt = 0
        for i in words:
            found = True
            for j in i:
                if not j  in st:
                    found = False
                    break
            if found:
                cnt+=1
        return cnt