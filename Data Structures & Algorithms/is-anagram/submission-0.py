from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sm = Counter(s)
        tm = Counter(t)

        return sm == tm
        