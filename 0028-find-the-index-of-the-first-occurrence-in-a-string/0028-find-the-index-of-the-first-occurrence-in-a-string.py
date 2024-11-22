class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n = len(needle)
        len_hay = len(haystack)
        for i in range(len_hay-len_n+1):
            p = i
            found = True
            for j in range(len_n):
                if haystack[p] != needle[j]:
                    found = False
                    break
                p += 1 
            if found:
                return i
        return -1
