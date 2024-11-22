class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a=[]
        an=[]
        ans=[]
        p1=float("inf")
        p2=float("inf")
        for i in range(len(s)):
            
            if s[len(s)-1-i]==c:
                p1=len(s)-1-i
            a.append(p1)
            if s[i]==c:
                p2=i
            an.append(p2)
        a = a[::-1]
        for i in range(len(s)):
           b=min(abs(a[i]-i),abs(an[i]-i))
           ans.append(b)
        print(an,a)


           
                    
            



                
        
        return ans
