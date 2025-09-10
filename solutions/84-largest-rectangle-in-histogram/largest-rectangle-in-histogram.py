class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk = []
        heights = [0] + heights + [0]

        cmax = 0
        for ix, h in enumerate(heights):
            while stk and heights[stk[-1]] > h:
                hh = heights[stk.pop()]
                ww = (ix - 1) - stk[-1]
                cmax = max(cmax, ww * hh)
            stk.append(ix)
        
        return cmax