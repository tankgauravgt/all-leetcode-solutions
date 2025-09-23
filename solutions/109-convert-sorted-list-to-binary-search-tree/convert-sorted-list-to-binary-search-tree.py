# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def get_middle(node):
            prev = None
            slow = node
            fast = node
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow
        
        def make_tree(node):
            if not node:
                return None
            
            middle = get_middle(node)

            if node == middle:
                return TreeNode(middle.val)

            ltree = make_tree(node)
            rtree = make_tree(middle.next)

            return TreeNode(middle.val, ltree, rtree)
        
        return make_tree(head)