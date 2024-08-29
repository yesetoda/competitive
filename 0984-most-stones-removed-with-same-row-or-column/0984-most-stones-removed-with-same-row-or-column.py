class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        seenRow,seenCol = set(),set()
        cnt = 0
        for r,c in stones:
            if r in seenRow:
                cnt+=1
                seenCol.add(c)
            elif c in seenCol:
                cnt+=1
                seenRow.add(r)
            else:
                seenRow.add(r)
                seenCol.add(c)
        return cnt
            
        