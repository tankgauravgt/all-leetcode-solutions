# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = dummy = ListNode(-1)

        while list1 or list2:
            v1 = float('inf') if not list1 else list1.val
            v2 = float('inf') if not list2 else list2.val
            if v1 <= v2:
                dummy.next = ListNode(v1)
                list1 = list1.next
            else:
                dummy.next = ListNode(v2)
                list2 = list2.next
            dummy = dummy.next
        
        return head.next