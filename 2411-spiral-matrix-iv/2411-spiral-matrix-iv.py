# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        seen = set()
        mat = [[-1]*n for i in range(m)]
        def inbound(x,y):
            return 0<=x<m and 0<=y<n
        moves= [(0,1),(1,0),(0,-1),(-1,0)]
        dir = ["left","down","right","down"]
        ind = 0
        cnt = 0
        cur = head
        a,b = 0,0
        times = 0
        while cur and cnt<n*m:
            if (a,b) not in seen and inbound(a,b):
                cnt+=1
                mat[a][b] = cur.val
                seen.add((a,b))
                cur = cur.next
                na,nb = moves[ind]
                if inbound(a+na,b+nb) and (a+na,b+nb) not in seen:
                    a,b = a+na, b+nb
            else:
                ind = (ind+1)%4
                na,nb = moves[ind]
                ax,by = a+na,b+nb
                if (ax,by) not in seen and inbound(ax,by):
                    a,b = ax,by
        return mat
            
            

        