class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ix = 0
        lx = 0
        rx = len(nums) - 1
        while ix <= rx:
            if nums[ix] == 0:
                nums[lx], nums[ix] = nums[ix], nums[lx]
                lx = lx + 1
                ix = ix + 1
            elif nums[ix] == 1:
                ix = ix + 1
            else:
                nums[ix], nums[rx] = nums[rx], nums[ix]
                rx = rx - 1