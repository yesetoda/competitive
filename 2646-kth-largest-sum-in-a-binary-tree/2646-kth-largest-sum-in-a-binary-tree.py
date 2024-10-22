# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelsum = Counter()
        def dfs(node,level):
            if node:
                levelsum[level]+=node.val
                dfs(node.left,level+1)
                dfs(node.right,level+1)
        dfs(root,1)
        if len(levelsum)<k:
            return -1
        else:
            return levelsum.most_common(k)[-1][1]

        