# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def rec(node, csum, buf, res):

            # do not run at null node:
            if not node:
                return
            
            csum = csum + node.val
            
            # run at leaf node:
            if not node.left and not node.right:
                buf.append(node.val)
                if csum == targetSum:
                    res.append(buf.copy())
                buf.pop()
                return
            
            buf.append(node.val)
            rec(node.left, csum, buf, res)
            rec(node.right, csum, buf, res)
            buf.pop()
        
        result = []
        rec(root, 0, [], result)
        return result