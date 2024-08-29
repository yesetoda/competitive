# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(node):
            nonlocal ans
            # if not ans:
            #     return 0
            if node:
                l = r = 0
                if node.left:
                    l = 1+ dfs(node.left)
                if node.right:
                    r = 1+ dfs(node.right)
                val = abs(l-r)
                if val >1:
                    ans = False
                    # return 0
                return max(l,r)
        dfs(root)
        return ans

                    
           