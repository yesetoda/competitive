class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pt1 = 0
        pt2 = 0
        candidate = -1
        cnt = 0
        while pt1<len(haystack):
            if pt2>0:
                if haystack[pt1] == needle[0]:
                    if candidate<0:
                        candidate = pt1
            if pt2==len(needle):
                return pt1-pt2
            if haystack[pt1] == needle[pt2]:
                pt1+=1
                pt2+=1
            else:
                if candidate>0:
                    pt1 = candidate
                    candidate = -1
                else:
                    pt1+=1
                pt2 = 0
            cnt+=1

        if pt2==len(needle):
            return pt1-pt2
        return -1
