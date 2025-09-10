# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(po, io, iol, ior, pol, por):
            if iol > ior:
                return None
            idx = io.index(po[pol], iol, ior + 1)
            ltree = build(po, io, iol, idx - 1, 1 + pol, 1 + pol + idx - iol)
            rtree = build(po, io, 1 + idx, ior, 1 + pol + idx - iol, por)
            cnode = TreeNode(po[pol], ltree, rtree)
            return cnode
        
        return build(preorder, inorder, 0, len(inorder) - 1, 0, len(preorder) - 1)