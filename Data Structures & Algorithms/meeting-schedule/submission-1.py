"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)

        if len(intervals) <= 1:
            return True

        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev.end > curr.start:
                return False

            prev = curr


        print(intervals)

        return True
        
