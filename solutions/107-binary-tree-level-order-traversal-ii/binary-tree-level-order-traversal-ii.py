from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dq = deque([root])

        res = deque()
        while dq:
            N = len(dq)
            temp = []
            for _ in range(N):
                curr = dq.popleft()
                if not curr:
                    continue
                temp.append(curr.val)
                dq.append(curr.left)
                dq.append(curr.right)
            if temp:
                res.appendleft(temp)
        
        return list(res)