class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        p = 0
        l1,l2 = len(str1),len(str2)
        ans = 0
        while p<min(l1,l2):
            if str1[p]!=str2[p]:
                break
            else:
                val = str1[:p+1]
                c1 = str1.count(val)
                c2 = str2.count(val)
                if len(str1) == (p+1)*c1 and len(str2) == (p+1)*c2:
                    ans = p+1
            p+=1
        return str1[:ans]


