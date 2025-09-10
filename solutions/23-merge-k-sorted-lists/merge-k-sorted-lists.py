# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.merge_range(lists, 0, len(lists) - 1)
    
    def merge_range(self, lists, lx, rx):
        if lx == rx:
            return lists[lx]
        mx = lx + (rx - lx) // 2
        left = self.merge_range(lists, lx, mx)
        right = self.merge_range(lists, mx + 1, rx)
        return self.merge_two(left, right)
    
    def merge_two(self, l1, l2):
        head = temp = ListNode(-1)
        while l1 or l2:
            v1 = float('inf') if not l1 else l1.val
            v2 = float('inf') if not l2 else l2.val
            if v1 <= v2:
                temp.next = ListNode(v1)
                l1 = l1.next
            else:
                temp.next = ListNode(v2)
                l2 = l2.next
            temp = temp.next
        return head.next