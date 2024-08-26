"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def traverse(root):
            if root:
                # print("this is the root",root.val)
                for i in root.children:
                    traverse(i)
                    ans.append(i.val)
                
        traverse(root)
        if root:
            ans.append(root.val)
        return ans