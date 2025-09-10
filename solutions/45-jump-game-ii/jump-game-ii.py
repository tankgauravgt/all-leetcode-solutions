class Solution:
    def jump(self, nums: List[int]) -> int:
        

        cmax = 0
        jumps = 0
        max_reach = 0
        for ix in range(len(nums) - 1):
            # scan in current receptive window. 
            # in this case, unconditionally.
            cmax = max(cmax, ix + nums[ix])

            # update max_reach found in current receptive field:
            if ix == max_reach:
                max_reach = cmax
                jumps = jumps + 1
        
        return jumps