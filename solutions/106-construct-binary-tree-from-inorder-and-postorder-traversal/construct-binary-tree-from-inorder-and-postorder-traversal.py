# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def rec(io, po):
            if not po:
                return None
            ix = io.index(po[-1])
            return TreeNode(
                po[-1],
                rec(io[0:ix], po[0:ix]),
                rec(io[1+ix:], po[ix:-1])
            )
        return rec(inorder, postorder)