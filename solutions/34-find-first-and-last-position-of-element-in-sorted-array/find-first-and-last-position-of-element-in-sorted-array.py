import bisect

class Solution:
    def searchRange(self, nums, target):
        def findPosition(isFirst):
            left, right = 0, len(nums) - 1
            position = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    position = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return position

        first = findPosition(True)
        last = findPosition(False)
        return [first, last]