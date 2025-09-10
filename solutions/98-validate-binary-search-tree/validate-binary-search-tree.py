# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        @cache
        def valid(node, lmax, rmin):
            if not node:
                return True
            if lmax < node.val < rmin:
                return valid(node.left, lmax, node.val) and valid(node.right, node.val, rmin)
            return False

        return valid(root, float('-inf'), float('+inf'))