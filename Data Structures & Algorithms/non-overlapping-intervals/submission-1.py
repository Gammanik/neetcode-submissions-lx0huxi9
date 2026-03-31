class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)

        prevEnd = intervals[0][1]
        i = 1
        while i < len(intervals):
            while i < len(intervals) and intervals[i][0] < prevEnd:
                prevEnd = min(prevEnd, intervals[i][1])
                intervals.pop(i)

            if i < len(intervals):
                prevEnd = intervals[i][1]
            i += 1

        print(intervals)
        return n - len(intervals)