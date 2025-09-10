# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        for ix in range(n):
            temp = temp.next
        
        if not temp:
            return head.next

        curr = head
        while temp and temp.next:
            curr = curr.next
            temp = temp.next
        curr.next = curr.next.next

        return head