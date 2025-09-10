import math

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        for ix in range(N - 3, -1, -1):
            if nums[ix] == nums[ix + 1] == nums[ix + 2]:
                nums[ix + 2] = float('nan')

        lx = 0
        for ix in range(N):
            if math.isnan(nums[ix]):
                continue
            nums[lx] = nums[ix]
            lx = lx + 1
            
        return lx