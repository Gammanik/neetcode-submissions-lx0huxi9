from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for n in nums:
            if not m[n]:
                m[n] = 0
            m[n] += 1

        print(m)

        sorted_map = dict(sorted(m.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_map)
        return list(sorted_map.keys())[:k]



        