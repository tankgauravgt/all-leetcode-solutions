# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        cmax = float('-inf')

        @cache
        def rec(node):
            nonlocal cmax
            if not node:
                return 0
            lmax = max(0, rec(node.left))
            rmax = max(0, rec(node.right))
            cmax = max(cmax, node.val + lmax + rmax)
            return node.val + max(lmax, rmax)
        
        rec(root)
        return cmax