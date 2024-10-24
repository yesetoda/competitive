class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,k = len(haystack),len(needle)
        a , b = 3 , 10**9+7
        alphas = [pow(a,k-i-1,b) for i in range(k)]
        def char_val(x):
            return ord(x)-96
        def pollFirst(hash,sv):
            return ( hash- alphas[ 0 ] * sv ) % b
        def addLast(hash,sv):
            return (hash*a +  sv ) % b
        vals = mine = 0
        if k>n:
            return -1
        for i in range(k):
            vals = addLast(vals,char_val(needle[i]))
            mine =  addLast(mine,char_val(haystack[i]))
        for i in range(k,n):
            if mine == vals:
                return i-k
            mine =  pollFirst(mine,char_val(haystack[i-k]))
            mine =  addLast(mine,char_val(haystack[i]))
        if mine == vals:
            return n-k
        return -1
            
