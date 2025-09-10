class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)

        intervals.sort()


        out = []
        prev = intervals[0]
        for ix in range(0, N, 1):
            if ix == 0:
                out.append(intervals[ix])
                continue
            curr = intervals[ix]
            if prev[1] >= curr[0]:
                prev[0] = min(prev[0], curr[0])
                prev[1] = max(prev[1], curr[1])
                continue
            out.append(curr)
            prev = curr

        return out