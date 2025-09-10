class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)

        def rec(sx, buf, res):
            if sx == N:
                res.append(buf.copy())
                return
            buf.append(nums[sx])
            rec(sx + 1, buf, res)
            buf.pop()
            rec(sx + 1, buf, res)
        
        result = []
        rec(0, [], result)
        return result