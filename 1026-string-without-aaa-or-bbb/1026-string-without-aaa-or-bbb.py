class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        while a>0 or b>0:
            if a>=b:
                ac = min(2,a)
                ans.append(ac*"a")
                a-=ac
                bc = min(a//(max(b,1)),1,b)
                ans.append(bc*"b")
                b-=bc
            else:
                bc = min(2,b)
                ans.append(bc*"b")
                b-=bc
                ac = min(b//(max(a,1)),1,a)
                ans.append(ac*"a")
                a-=ac
        return "".join(ans)
