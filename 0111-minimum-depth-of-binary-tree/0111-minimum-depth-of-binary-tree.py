# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node,depth):
            if node:
                if not node.right and not node.left:
                    return depth
                ans = float("inf")
                if node.left:
                    ans = min(ans,dfs(node.left,depth+1))
                if node.right:
                    ans = min(ans, dfs(node.right,depth+1))
                return ans
            return 0
        ans = dfs(root,1)
        return ans
                