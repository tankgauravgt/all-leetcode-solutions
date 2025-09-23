# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def rec(node, csum, tgt):

            # do not run at null node:
            if not node:
                return False

            csum = csum + node.val

            # run at leaf node:
            if not node.left and not node.right:
                return csum == tgt

            flag = False
            flag = flag or rec(node.left, csum, tgt)
            flag = flag or rec(node.right, csum, tgt)
            return flag
        
        return rec(root, 0, targetSum)