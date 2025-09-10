# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = temp = ListNode(-1, head)

        while temp and temp.next and temp.next.next:
            if temp.next.val == temp.next.next.val:
                temp2 = temp.next
                while temp2 and temp2.next and temp2.val == temp2.next.val:
                    temp2 = temp2.next
                temp.next = temp2.next
            else:
                temp = temp.next
        
        return dummy.next