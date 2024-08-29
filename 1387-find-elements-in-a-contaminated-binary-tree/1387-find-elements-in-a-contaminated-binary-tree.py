# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
        
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        root.val = 0
        self.seen.add(0)
        self.traverse(root)


    def traverse(self,node):
        if node.left:
            node.left.val = node.val*2+1
            self.seen.add(node.left.val)
            self.traverse(node.left)
        if node.right:
            node.right.val = node.val*2+2
            self.seen.add(node.right.val)
            self.traverse(node.right)
    def find(self, target: int) -> bool:
        return target in self.seen
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)