# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        head1 = temp1 = ListNode()
        head2 = temp2 = ListNode()

        temp = head
        while temp:
            next_node = temp.next
            if temp.val < x:
                temp1.next = temp
                temp1 = temp1.next
                temp.next = None
            else:
                temp2.next = temp
                temp2 = temp2.next
                temp.next = None
            temp = next_node

        temp1.next = head2.next

        return head1.next