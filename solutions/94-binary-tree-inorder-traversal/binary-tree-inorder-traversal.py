# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def iot(root):
            curr = root
            stk, out = [], []
            while curr or stk:
                while curr:
                    stk.append(curr)
                    curr = curr.left
                curr = stk.pop()
                out.append(curr.val)
                curr = curr.right
            return out
        
        return iot(root)