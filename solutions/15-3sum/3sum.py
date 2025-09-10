class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)        
        nums.sort()

        result = []
        for ix in range(N - 2):
            if ix > 0 and nums[ix - 1] == nums[ix]:
                continue
            jx = ix + 1
            kx = N - 1
            while jx < kx:
                s = nums[ix] + nums[jx] + nums[kx]
                if s < 0:
                    while jx < kx and nums[jx] == nums[jx + 1]:
                        jx = jx + 1
                    jx = jx + 1
                elif s > 0:
                    while kx > jx and nums[kx] == nums[kx - 1]:
                        kx = kx - 1
                    kx = kx - 1
                else:
                    result.append([nums[ix], nums[jx], nums[kx]])
                    while jx < kx and nums[jx] == nums[jx + 1]:
                        jx = jx + 1
                    jx = jx + 1
        
        return result