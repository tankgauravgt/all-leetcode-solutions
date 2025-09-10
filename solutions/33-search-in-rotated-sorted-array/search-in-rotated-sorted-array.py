import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ix = bisect.bisect_left(nums, 0.5, key=lambda x: int(x < nums[0]))
        imap = lambda x: (x + ix) % N
        
        def bsearch(arr, lx, rx, tgt):
            while lx <= rx:
                mx = lx + (rx - lx) // 2
                if arr[imap(mx)] == tgt:
                    return imap(mx)
                elif arr[imap(mx)] < tgt:
                    lx = mx + 1
                else:
                    rx = mx - 1
            return -1
        
        return bsearch(nums, 0, N, target)