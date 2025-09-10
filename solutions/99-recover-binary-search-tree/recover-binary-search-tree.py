# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.e1 = None
        self.e2 = None
        self.prev = TreeNode(float('-inf'))
    

    def recoverTree(self, root):
        self.traverse(root)
        self.e1.val, self.e2.val = self.e2.val, self.e1.val
    

    def traverse(self, root):
        if not root:
            return
        
        self.traverse(root.left)
        
        # >>> business logic start
        if not self.e1 and self.prev.val >= root.val:
            self.e1 = self.prev
        if self.e1 and self.prev.val >= root.val:
            self.e2 = root
        # <<< business logic end

        self.prev = root
        self.traverse(root.right)