"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nxt = [None]*6000
        def dfs(node,depth):
            if node:
                if node.right:
                    x = node.right
                    x.next = nxt[depth]
                    nxt[depth] = x
                    dfs(x,depth+1)
                if node.left:
                    x = node.left
                    x.next = nxt[depth]
                    nxt[depth] = x
                    dfs(x,depth+1)
        dfs(root,0)
        return root
                