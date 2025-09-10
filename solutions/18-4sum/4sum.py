class Solution:
    def fourSum(self, nums, target):
        
        if len(nums) < 4:
            return []
            
        nums.sort()
        
        N = len(nums)
        
        result = []
        for x1 in range(0, N, 1):
            
            if x1 > 0 and nums[x1 - 1] == nums[x1]:
                continue
            
            for x2 in range(1 + x1, N, 1):                
                if x2 > 1 + x1 and nums[x2 - 1] == nums[x2]:
                    continue
                
                x3 = x2 + 1
                x4 = N - 1
                
                while x3 < x4:
                
                    S = nums[x1] + nums[x2] + nums[x3] + nums[x4]
                    
                    if S < target:
                        x3 = x3 + 1
                        
                    elif S > target:
                        x4 = x4 - 1
                        
                    else:
                        result.append([nums[x1], nums[x2], nums[x3], nums[x4]])
                        while x3 < x4 and nums[x3] == nums[1 + x3]:
                            x3 = x3 + 1
                        x3 = x3 + 1
                        
        return result