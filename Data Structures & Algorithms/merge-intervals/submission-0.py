class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        n = len(intervals)
        res = []

        i = 0
        while i < n:
            s, e = intervals[i]

            j = i+1
            while j < n and intervals[j][0] <= e:
                e = max(e, intervals[j][1])
                j += 1


            res.append([s,e])
            i = j


        return res

