# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        while q:
            pre = []
            sm = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    pre.append([node,0])
                    if node.left:
                        q.append(node.left)
                        pre[-1][1] += node.left.val
                    if node.right:
                        q.append(node.right)
                        pre[-1][1] += node.right.val
                    sm+=pre[-1][1]
            for n,v in pre:
                if n.left:
                    n.left.val = sm-v
                if n.right:
                    n.right.val = sm-v
        root.val = 0
        return root
            

                
            
                   