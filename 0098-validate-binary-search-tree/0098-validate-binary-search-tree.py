# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(node,mn,mx):
            nonlocal ans
            if not ans:
                return
            if node:
                print(mn,node.val,mx)
                if node.val<=mn or node.val>=mx:
                    ans = False
                    return
                if node.left:
                    dfs(node.left,mn,node.val)
                if node.right:
                    dfs(node.right,node.val,mx)
        dfs(root,-float(inf),float("inf"))
        return ans
        