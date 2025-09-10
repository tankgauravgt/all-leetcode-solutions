# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        head = temp = ListNode(-1, head)

        while temp and temp.next and temp.next.next:
            node_plus_1 = temp.next
            node_plus_2 = temp.next.next
            node_plus_3 = temp.next.next.next

            node_plus_1.next = node_plus_3
            node_plus_2.next = node_plus_1
            temp.next = node_plus_2
            
            temp = temp.next.next
        
        return head.next