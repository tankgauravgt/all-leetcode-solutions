class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        lx = 0
        rx = len(nums) - 1

        while lx <= rx:
            
            mx = lx + (rx - lx) // 2
            
            if nums[mx] == target:
                return True
            
            if nums[lx] == nums[mx] == nums[rx]:
                lx = lx + 1
                rx = rx - 1
            
            elif nums[lx] <= nums[mx]:
                if nums[lx] <= target <= nums[mx]:
                    rx = mx - 1
                else:
                    lx = mx + 1
            
            else:
                if nums[mx] <= target <= nums[rx]:
                    lx = mx + 1
                else:
                    rx = mx - 1
        
        return False