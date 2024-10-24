class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b == "":
            return 0
        else:
            times = len(b)//len(a)+2
            if times == 0:
                return -1
            else:
                na = a*times
                lsp = [0]
                l,r = 0,1
                aleng,bleng = len(na),len(b) 
                while r<bleng:
                    if na[l] == b[r]:
                        lsp.append(l+1)
                        l+=1
                        r+=1
                    elif l>0:
                        l = lsp[l-1]
                    else:
                        r+=1
                        lsp.append(0)
                i,j = 0,0
                ans = -1
                while i<aleng:
                    if j == len(b):
                        ans = i
                        break
                    if na[i] == b[j]:
                        i+=1
                        j+=1
                    elif j>0:
                        j = lsp[j-1]
                    else:
                        i+=1
                if j == bleng:
                    ans = i
                if ans == -1:
                    return -1
                else:
                    tm = math.ceil(ans/len(a))
                    return int(tm)

                    

