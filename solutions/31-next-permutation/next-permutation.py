class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def find_pivot(arr):
            N = len(arr)
            for ix in range(N - 2, -1, -1):
                if arr[ix] < arr[ix + 1]:
                    return ix
            return -1
        
        def swap_min_and_reverse(arr, px):
            if px == -1:
                arr.reverse()
                return
            N = len(arr)
            for ix in range(N - 1, px, -1):
                if arr[ix] > arr[px]:
                    arr[ix], arr[px] = arr[px], arr[ix]
                    arr[px + 1::] = reversed(arr[px + 1::])
                    break
        
        index = find_pivot(nums)
        swap_min_and_reverse(nums, index)