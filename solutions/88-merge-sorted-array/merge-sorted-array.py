import heapq

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1

        fx = m + n - 1
        while p1 >= 0 or p2 >= 0:

            t1 = -float('inf') if p1 < 0 else nums1[p1]
            t2 = -float('inf') if p2 < 0 else nums2[p2]
            
            if t1 >= t2:
                nums1[fx] = t1
                p1 = p1 - 1
            elif t2 > t1:
                nums1[fx] = t2
                p2 = p2 - 1
            
            fx = fx - 1