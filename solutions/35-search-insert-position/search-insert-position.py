import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lx = 0
        rx = len(nums)
        while lx < rx:
            mx = lx + (rx - lx) // 2
            if nums[mx] < target:
                lx = mx + 1
            else:
                rx = mx
        return lx