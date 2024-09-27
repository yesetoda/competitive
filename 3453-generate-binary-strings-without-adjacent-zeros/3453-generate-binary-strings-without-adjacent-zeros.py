class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = deque([["0"],["1"]])
        while n-1>0:
            leng = len(ans)
            for i in range(leng):
                cur = ans.popleft()
                if cur[-1] == "0":
                    cur.append("1")
                    ans.append(cur)
                else:
                    ans.append(cur+["0"])
                    ans.append(cur+["1"])
            n-=1
        out = []
        for i in ans:
            out.append("".join(i))


        return out