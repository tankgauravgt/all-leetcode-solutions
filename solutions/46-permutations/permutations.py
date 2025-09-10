class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        nums = set(nums)

        N = len(nums)
        def rec(buf, vset, res):
            if len(buf) == N:
                res.append(buf.copy())
                return
            for n in nums:
                if n not in vset:
                    buf.append(n)
                    vset.add(n)
                    rec(buf, vset, res)
                    vset.remove(n)
                    buf.pop()
        
        result = []
        rec([], set(), result)
        return result