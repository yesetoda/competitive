# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node,path,sm):
            if node:
                if node.left:
                    dfs(node.left,path+[node.left.val],sm+node.left.val)
                if node.right:
                    dfs(node.right,path+[node.right.val],sm+node.right.val)
                if sm == targetSum:
                    if not node.left and not node.right:
                        ans.append(path[:])
        dfs(root,[root.val] if root else [],(root.val if root else 0))
        return ans


