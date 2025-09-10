# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        rlast = head
        while rlast and rlast.next:
            rlast = rlast.next

        n = 0
        temp = head
        while temp:
            temp = temp.next
            n = n + 1

        if not head or not head.next:
            return head

        for ix in range(n - (k % n)):
            curr = head
            head = curr.next
            curr.next = None
            rlast.next = curr
            rlast = rlast.next
        
        return head