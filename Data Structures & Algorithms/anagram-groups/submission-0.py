class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for el in strs:
            key = "".join(sorted(el))
            if key not in d:
                d[key] = []

            d[key].append(el)

        return list(d.values())
        