class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)

        lmax = [0 for ix in range(N + 1)]
        rmax = [0 for ix in range(N + 1)]
        
        for ix in range(N):
            lmax[ix + 1] = max(lmax[ix], height[ix])
        
        for ix in range(N - 1, -1, -1):
            rmax[ix] = max(rmax[ix + 1], height[ix])

        total = 0
        for ix in range(N):
            total = total + max(0, min(lmax[ix], rmax[ix]) - height[ix])

        return total