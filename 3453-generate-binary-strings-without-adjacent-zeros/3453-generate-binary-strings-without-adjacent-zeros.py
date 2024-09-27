class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def rec(n,path):
            if n == 0:
                ans.append("".join(path))
                return 
            for i in range(2):
                if path and path[-1] == "0":
                    if i == 0:
                        pass
                    else:
                        path.append(str(i))
                        rec(n-1,path)
                        path.pop()
                else:
                    path.append(str(i))
                    rec(n-1,path)
                    path.pop()
        rec(n,[])
        return ans