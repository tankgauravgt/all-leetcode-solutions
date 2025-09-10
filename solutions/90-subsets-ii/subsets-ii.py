class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        def rec(sx, arr, curr, res):
            res.append(curr.copy())
            for ix in range(sx, len(arr), 1):
                if ix > sx and arr[ix] == arr[ix - 1]: continue
                curr.append(arr[ix])
                rec(1 + ix, arr, curr, res)
                curr.pop()
        
        result = []
        rec(0, nums, [], result)
        return result