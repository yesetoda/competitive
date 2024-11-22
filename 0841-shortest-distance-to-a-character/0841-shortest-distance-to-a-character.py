class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a=[]
        an=[]
        for i in range(len(s)):
            if s[i]==c:
                a.append(i)
        for i in range(len(s)):
            p=len(s)
            
            for j in range(len(a)):
                if abs(i-a[j])<p:
                    p=abs(i-a[j])
            an.append(p)
                    
            



                
        print(an)
        return an
