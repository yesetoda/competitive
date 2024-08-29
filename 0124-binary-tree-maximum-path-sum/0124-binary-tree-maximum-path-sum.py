# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = -float("inf")
        def dfs(node):
            nonlocal mx
            if node:
                val = 0
                if node.left:
                    lft  = dfs(node.left)
                if node.right:
                    rit =  dfs(node.right)

              
                if node.left and node.right:
                    mx = max(mx,node.val,lft,rit,node.val+rit+lft)
                    node.val += max(rit,lft,0)
                elif node.left:
                    mx = max(mx,node.val,lft,node.val+lft)
                    node.val += max(0,lft)
                elif node.right:
                    mx = max(mx,node.val,rit,node.val+rit)
                    node.val += max(0,rit)
                return node.val
            return 0
        dfs(root)
        mx = max(mx,root.val)
        return mx


           
            


        