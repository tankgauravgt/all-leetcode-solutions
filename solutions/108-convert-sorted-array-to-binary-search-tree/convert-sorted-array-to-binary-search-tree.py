# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def rec(arr, lx, rx):
            if lx > rx:
                return None
            mx = lx + (rx - lx) // 2
            ltree = rec(arr, lx, mx - 1)
            rtree = rec(arr, mx + 1, rx)
            return TreeNode(nums[mx], ltree, rtree)
        
        return rec(nums, 0, len(nums) - 1)