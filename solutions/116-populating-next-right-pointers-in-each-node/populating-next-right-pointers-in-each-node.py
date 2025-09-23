from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return root

        dq = deque([root])

        while dq:
            N = len(dq)
            for ix in range(N - 1):
                dq[ix].next = dq[ix + 1]
            dq[N - 1].next = None
            for _ in range(N):
                cnode = dq.popleft()
                if cnode.left:
                    dq.append(cnode.left)
                if cnode.right:
                    dq.append(cnode.right)
            
        return root