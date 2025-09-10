class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        cmax = 0
        for ix in range(N):
            if ix > cmax:
                return False
            cmax = max(cmax, ix + nums[ix])
        return True