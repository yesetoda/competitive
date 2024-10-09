# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(x,cnt):
            last = x
            cur = x
            nxt = cur.next
            prev = None
            order = []
            while cur and cnt>0:
                nxt = cur.next
                order.append(cur.val)
                cur.next = prev
                prev = cur
                cur = nxt 
                cnt-=1
            if cnt == 0:
                return prev,last,nxt
            else:
                node = ListNode(order[0])
                cur = node
                for i in range(1,len(order)):
                    cur.next = ListNode(order[i])
                    cur = cur.next
                return node,None,None
        dummy = ListNode(-1)
        dcur = dummy
        cur = head
        while cur:
            current,last,nxt = reverse(cur,k)
            dcur.next = current
            dcur = last
            cur = nxt        
            


        return dummy.next

                


        