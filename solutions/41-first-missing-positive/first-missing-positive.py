class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        # Steps:
        # ------
        # 1. Perform cyclic sort (arr[ix] = ix + 1)
        # 2. Write a checking loop

        # =================================================
        # perform cyclic sort:
        # =================================================

        ix = 0
        while ix < N:
            correct = nums[ix] - 1
            if 0 <= correct < N and nums[ix] != nums[correct]:
                nums[ix], nums[correct] = nums[correct], nums[ix]
                continue
            ix = ix + 1
        
        # =================================================
        # checking loop:
        # =================================================

        for ix in range(N):
            if nums[ix] != ix + 1:
                return ix + 1
        
        return N + 1