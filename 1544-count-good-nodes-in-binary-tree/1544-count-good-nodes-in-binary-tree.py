# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([root])
        ans = 0
        while q:
            ln = len(q)
            for _ in range(ln):
                node = q.popleft()
                if node.left:
                    lft = node.left
                    lval = lft.val
                    if node.val<=lval:
                        ans+=1
                    lft.val = max(node.val,lval)
                    q.append(lft)
                if node.right:
                    rit = node.right
                    rval = rit.val
                    if node.val<=rval:
                        ans+=1
                    rit.val = max(node.val,rval)
                    q.append(rit)
        return ans+1