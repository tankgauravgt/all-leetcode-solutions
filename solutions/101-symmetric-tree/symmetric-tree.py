# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        @cache
        def rec(n1, n2):
            if not n2:
                return n1 == None
            if not n1:
                return n2 == None
            return n1.val == n2.val and rec(n1.left, n2.right) and rec(n1.right, n2.left)
        
        return rec(root, root)