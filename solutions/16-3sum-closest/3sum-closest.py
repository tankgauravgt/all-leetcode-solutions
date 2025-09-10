class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        cmin = float('inf')
        for ix in range(len(nums) - 2):
            lx = ix + 1
            rx = len(nums) - 1
            while lx < rx:
                s = nums[ix] + nums[lx] + nums[rx]
                if s == target: 
	                return s
                cmin = min(cmin, s, key=lambda x: abs(target - x))
                if s <= target:
                    lx += 1
                else:
                    rx -= 1
        return cmin