# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def rec(lx, rx):
            if lx <= rx:
                res = []
                for ix in range(lx, 1 + rx):
                    ltrees = rec(lx, ix - 1)
                    rtrees = rec(ix + 1, rx)
                    for ltree in ltrees:
                        for rtree in rtrees:
                            res.append(TreeNode(ix, ltree, rtree))
                return res
            return [None]
        
        return rec(1, n)