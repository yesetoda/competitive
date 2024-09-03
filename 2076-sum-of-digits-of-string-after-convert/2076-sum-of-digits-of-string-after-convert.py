class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dig = []
        for i in s:
            for j in str(ord(i)-96):
                dig.append(int(j))
        
        for i in range(k):
            sm = 0
            for j in dig:
                sm+=int(j)
            dig = [int(i) for i in str(sm)]
        return sm
