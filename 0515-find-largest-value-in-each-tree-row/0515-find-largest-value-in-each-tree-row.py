# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = deque([root]) if root else None
        while q:
            ln = len(q)
            x = -float("inf")
            for i in range(ln):
                node = q.popleft()
                x = max(x,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(x)
        return ans
                



            
           