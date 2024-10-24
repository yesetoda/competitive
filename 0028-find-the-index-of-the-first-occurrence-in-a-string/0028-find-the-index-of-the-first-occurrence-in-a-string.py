class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a,b = 0,1
        lsp =[0]
        nleng,hleng = len(needle),len(haystack)
        while b<nleng:
            if needle[a] == needle[b]:
                lsp.append(a+1)
                a+=1
                b+=1
            elif a>0:
                a = lsp[a-1]
            else:
                b+=1
                lsp.append(0)
        i = j = 0
        ans = -1
        while i<hleng:
            if j == nleng:
                ans = i-j
                break
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            elif j>0:
                j = lsp[j-1]
            else:
                i+=1
        if j == nleng:
            ans = i-j

        return ans