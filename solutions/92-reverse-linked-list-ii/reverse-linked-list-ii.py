# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def revk(node, k):
            prev = None
            curr = node
            while curr and k > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k = k - 1
            return prev, curr, k > 0

        h1 = temp = ListNode(-1, head)
        for _ in range(left - 1):
            temp = temp.next

        h2, h3, _ = revk(temp.next, right - left + 1)

        temp.next = h2
        while temp and temp.next: 
            temp = temp.next
        temp.next = h3

        return h1.next