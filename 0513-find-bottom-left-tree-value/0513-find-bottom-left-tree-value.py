# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # def dfs(level,node,ans):
        #     if node:
        #         if level>ans[0]:
        #             ans = [level,node.val]
        #         print(ans,node.val,level)
        #         if node.left:
        #             dfs(level+1,node.left,ans)
        #         if node.right:
        #             dfs(level+1,node.right,ans)
        #     return ans[1]
        # return dfs(0,root,[-1,-1])
        ans = -1
        q = deque([root])
        while q:
            ln = len(q)
            for i in range(ln):
                node = q.popleft()
                if i == 0:
                    ans = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
                



            
           