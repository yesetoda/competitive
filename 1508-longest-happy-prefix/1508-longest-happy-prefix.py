class Solution:
    def longestPrefix(self, s: str) -> str:
        lsp = [0]
        leng = len(s)
        i = 0
        j = 1
        while j<leng:
            if s[i] == s[j]:
                lsp.append(i+1)
                i+=1
                j+=1
            elif i>0:
                i = lsp[i-1]
            else:
                lsp.append(0)
                j+=1
        val = lsp[-1]
        return s[-lsp[-1]:] if val>0 else ""

