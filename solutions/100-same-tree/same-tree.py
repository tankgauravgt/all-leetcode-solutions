# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        @lru_cache(maxsize=None)
        def iot(n1, n2):
            if not n1 and not n2:
                return True
            if n1 and not n2:
                return False
            if not n1 and n2:
                return False
            return n1 and n2 and (n1.val == n2.val) and iot(n1.left, n2.left) and iot(n1.right, n2.right)
        
        return iot(p, q)