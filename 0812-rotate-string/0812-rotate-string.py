class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)>len(goal):
            return False
        s += s
        lsp = [0]
        l = 0
        r = 1
        while r<len(goal):
            if goal[l] == goal[r]:
                lsp.append(l+1)
                l+=1
                r+=1
            elif l>0:
                l = lsp[l-1]
            else:
                r+=1
                lsp.append(0)
        i,j = 0,0

        while i<len(s):
            if j>=len(lsp):
                return True
            if s[i] == goal[j]:
                i+=1
                j+=1
            elif j>0:
                j = lsp[j-1]
            else:
                i+=1
        return j>=len(goal)

        