# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(node1,node2):
            nonlocal ans
            if not ans:
                return ans
            if node1 and node2:
                if node1.val != node2.val:
                    ans = False
                    return 
                r,l = node1.right,node1.left
                r1,l1 = node2.right,node2.left
                if r:
                    if l1:
                        if r.val == l1.val:
                            node1.left = r
                            node1.right = l
                elif l:
                    if r1:
                        if l.val == r1.val:
                            node1.left = r
                            node1.right = l
                dfs(node1.left,node2.left)
                dfs(node1.right,node2.right)
            else:
                ans = not node1 and  not node2
        dfs(root1,root2)
        return ans