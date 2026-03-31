from sortedcontainers import SortedList

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.cnt = k, len(nums)
        self.s = SortedList(nums)    

    def add(self, val: int) -> int:
        self.s.add(val)
        self.cnt += 1
        k = min(self.k, self.cnt)
        return self.s[-k]
