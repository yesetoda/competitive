# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = False
        def dfs(node,sm):
            nonlocal ans
            if ans:
                return 
            if node:
                if node.left:
                    dfs(node.left,sm+node.left.val)
                    if ans:
                        return 
                if node.right:
                    dfs(node.right,sm+node.right.val)
                    if ans:
                        return 
                if not node.left and not node.right:
                    if sm == targetSum:
                        ans = True
                        return 
        dfs(root,root.val if root else 0)
        return ans

                