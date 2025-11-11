class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = {}
        for ix, n in enumerate(nums):
            if target - n not in rec:
                rec[n] = ix
                continue
            return [rec[target - n], ix]
        return [-1, -1]