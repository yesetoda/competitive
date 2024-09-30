class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key = len,reverse = True)
        leng = len(words)
        ans = 0
        for i in range(leng-1):
            if ans >= len(words[i])*len(words[i+1]):
                return ans
            for j in range(i+1,leng):
                if ans >= len(words[i])*len(words[j]):
                    break
                u = set(words[i]).intersection(set(words[j]))
                if not u:
                    ans = max(ans,len(words[i])*len(words[j]))
                    
        return ans
        