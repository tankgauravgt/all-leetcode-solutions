# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = temp = ListNode(-1, None)

        c = 0
        while l1 or l2:
            n1 = 0 if not l1 else l1.val
            n2 = 0 if not l2 else l2.val
            s = (n1 + n2 + c) % 10
            c = (n1 + n2 + c) // 10
            temp.next = ListNode(s)
            temp = temp.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next

        if c != 0:
            temp.next = ListNode(c)

        return head.next