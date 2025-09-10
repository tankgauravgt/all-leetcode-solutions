# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = temp = ListNode()

        c = 0
        while l1 or l2:
            v1 = (0 if not l1 else l1.val)
            v2 = (0 if not l2 else l2.val)
            s = v1 + v2 + c
            c = s // 10
            temp.next = ListNode(s % 10)
            temp = temp.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
        
        if c != 0:
            temp.next = ListNode(c)
        
        return head.next