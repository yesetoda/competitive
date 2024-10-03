# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        nxt = head.next
        while cur and cur.next:
            if cur.next.val != 0:
                cur.val += cur.next.val
                cur.next = cur.next.next
            else:
                if cur.next.next:
                    cur = cur.next
                else:
                    cur.next = None
                    break
        return head
