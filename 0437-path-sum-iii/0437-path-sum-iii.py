# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        if root:
            q = deque([[root,[targetSum - root.val]]])
            while q:
                ln = len(q)
                for _ in range(ln):
                    cur,vals = q.popleft()
                    for i in vals:
                        if i == 0:
                            ans+=1
                    if cur.left:
                        lval = cur.left.val
                        lvals = vals[:]
                        for i in range(len(vals)):
                            lvals[i]-=lval
                        lvals.append(targetSum-lval)
                        q.append([cur.left,lvals])
                    if cur.right:
                        rval = cur.right.val
                        rvals = vals[:]
                        for i in range(len(vals)):
                            rvals[i]-=rval
                        rvals.append(targetSum-rval)
                        q.append([cur.right,rvals])
        return ans
            

