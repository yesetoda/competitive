# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root
        def traverse(cur):
            if not cur:
                return
            if cur.left:
                traverse(cur.left)
            if cur.right:
                traverse(cur.right)
            ans.append(cur.val)
        traverse(cur)
        return ans