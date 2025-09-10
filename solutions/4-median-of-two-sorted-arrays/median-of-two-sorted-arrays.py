class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # keep smaller array above:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # get lengths of above and below arrays:
        nU, nL = len(nums1), len(nums2)        
        lx, rx = 0, nU

        while lx <= rx:

            # get partitions:
            px_u = (lx + rx) // 2
            px_l = (nU + nL + 1) // 2 - px_u

            # [...] - [<px_u>, ...]
            ul_max = float('-inf') if px_u == 0 else nums1[px_u - 1]
            ur_min = float('+inf') if px_u == nU else nums1[px_u]

            # [...] - [<px_l>, ...]
            ll_max = float('-inf') if px_l == 0 else nums2[px_l - 1]
            lr_min = float('+inf') if px_l == nL else nums2[px_l]

            
            # if already in equilibrium:
            if ul_max <= lr_min and ur_min >= ll_max:

                if (nL + nU) % 2 == 0:
                    return (max(ul_max, ll_max) + min(ur_min, lr_min)) / 2
                else:
                    return max(ul_max, ll_max)

            # not in equilibrium:
            elif ul_max > lr_min:
                rx = px_u - 1
            else:
                lx = px_u + 1
        
        return -1