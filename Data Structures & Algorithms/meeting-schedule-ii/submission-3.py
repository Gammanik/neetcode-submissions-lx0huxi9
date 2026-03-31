"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        s, e, n = 0, 0, len(intervals)
        res, cnt = 0, 0

        while e < n:
            while s < n and starts[s] < ends[e]:
                s += 1
                cnt += 1
                res = max(res, cnt)

            e += 1
            cnt -= 1

        return res