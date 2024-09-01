# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view  = [None]
        
        def dfs(node,depth):
            if node:
                if node.right:
                    if len(view)==depth:
                        view.append(node.right.val)
                    dfs(node.right,depth+1)
                if node.left:
                    if len(view)==depth:
                        view.append(node.left.val)
                    dfs(node.left,depth+1)
        if not root:
            return []
        dfs(root,1)
        view[0] = root.val
        return view


        