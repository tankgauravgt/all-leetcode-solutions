# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def rev_k(node, k):
            prev = None
            curr = node
            while curr and k > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k = k - 1
            return prev, curr, k == 0
        
        dummy = temp = ListNode(0)
        
        while head:
            done, head, completed = rev_k(head, k)
            temp.next = done if completed else rev_k(done, k)[0]
            while temp and temp.next:
                temp = temp.next
        
        return dummy.next