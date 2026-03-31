class TimeMap:

    def __init__(self):
        self.m = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.m.get(key):
            self.m[key] = [(value, timestamp)]
            return

        self.m[key].insert(0, (value, timestamp))
        # self.m[key] = sorted(self.m[key], key=lambda x: x[1], reverse = True)
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.m.get(key):
            return ""

        for el in self.m[key]:
            print(el)
            if el[1] <= timestamp:
                return el[0]

        return ""