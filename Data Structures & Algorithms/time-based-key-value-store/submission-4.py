from collections import deque

class TimeMap:

    def __init__(self):
        self.m = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.m.get(key):
            self.m[key] = deque([(value, timestamp)])
            return

        self.m[key].appendleft((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.m.get(key):
            return ""

        for el in self.m[key]:
            if el[1] <= timestamp:
                return el[0]

        return ""
