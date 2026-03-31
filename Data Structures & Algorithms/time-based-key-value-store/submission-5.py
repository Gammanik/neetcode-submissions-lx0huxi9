from collections import deque

class TimeMap:

    def __init__(self):
        self.m = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.m.get(key):
            self.m[key] = [(value, timestamp)]
            return

        self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.m.get(key):
            return ""

        arr = self.m[key]
        l, r = 0, len(arr)-1

        if timestamp < arr[l][1]:
            return ""

        print(arr)
        res = ""

        while l <= r:
            m = l + (r - l) // 2
            print(l, r, m)
            
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1

        return res


# [1, 2, 3, 4]