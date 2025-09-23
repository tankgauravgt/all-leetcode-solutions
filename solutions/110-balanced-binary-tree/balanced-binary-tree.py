# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getH(node):
            if not node:
                return 0
            lH = getH(node.left)
            rH = getH(node.right)
            if lH == -1 or rH == -1:
                return -1
            if abs(lH - rH) > 1:
                return -1
            return 1 + max(lH, rH)
        
        return getH(root) != -1