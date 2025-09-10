class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        lx = 0
        rx = len(height) - 1

        cmax = 0
        while lx <= rx:
            if height[lx] <= height[rx]:
                cmax = max(cmax, min(height[lx], height[rx]) * (rx - lx))
                lx = lx + 1
            else:
                cmax = max(cmax, min(height[lx], height[rx]) * (rx - lx))
                rx = rx - 1
        
        return cmax