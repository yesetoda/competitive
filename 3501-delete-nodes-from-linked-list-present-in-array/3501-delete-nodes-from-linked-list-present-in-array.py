# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        x = ans = ListNode(-1,head)
        st = set(nums)
        while x:
            while x.next and x.next.val in st:
                y = x.next.next
                x.next = y
            x = x.next
        return ans.next
        

