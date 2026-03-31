class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_s, n_e = newInterval
        res = []
        print(n_s, n_e)

        i = 0
        while i < len(intervals) and intervals[i][1] < n_s:
            res.append(intervals[i])
            i += 1

        # if i == len(intervals):
        #     res.append(newInterval)
        #     return res

        upd_s, upd_e = -1, -1
        idx = i
        while i < len(intervals) and intervals[i][0] <= n_e:
            upd_s, upd_e = min(n_s, intervals[idx][0]), max(intervals[i][1], n_e)
            i += 1

        if upd_s != -1:
            res.append([upd_s, upd_e])
        else:
            res.append(newInterval)
        

        while i < len(intervals):
            res.append(intervals[i])
            i += 1


        return res