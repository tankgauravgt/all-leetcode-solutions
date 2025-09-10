import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)

        ix = 0
        flag = False
        while ix < len(intervals):
            if ix == 0:
                ix = ix + 1
                continue
            if intervals[ix - 1][1] >= intervals[ix][0]:
                intervals[ix - 1][0] = min(intervals[ix - 1][0], intervals[ix][0])
                intervals[ix - 1][1] = max(intervals[ix - 1][1], intervals[ix][1])
                intervals.pop(ix)
                continue
            ix = ix + 1
        
        return intervals