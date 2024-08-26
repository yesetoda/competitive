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
        q = [root]
        seen = set()
        while q:
            while q and q[-1] and len(q[-1].children)>0:
                if not q[-1] in seen:
                    seen.add(q[-1])
                    q.extend(q[-1].children[::-1])
                else:
                    ans.append(q.pop().val)
            else:
                if q and q[-1]:
                    ans.append(q.pop().val)
                else:break
        return ans