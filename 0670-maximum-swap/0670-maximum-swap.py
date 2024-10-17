class Solution:
    def maximumSwap(self, num: int) -> int:
        s1 = str(num)
        ln = len(s1)
        s = sorted(str(num),reverse=True)
        ans = list(s1)
        rem = ""
        chg = ""
        for i in range(ln):
            ans[i] = s[i]
            if s1[i] != s[i]:
                rem = s1[i]
                chg = s[i]
                break
        if len(rem)>0:
            for i in range(ln-1,-1,-1):
                if ans[i] == chg:
                    ans[i] = rem
                    break
        return int(''.join(ans))


