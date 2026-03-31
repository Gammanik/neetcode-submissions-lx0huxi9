from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        m1, m2 = Counter(t), {}
        need, have = len(m1), 0
        i, j = 0, 0
        i_res, j_res, res = 0, 0, 1001

        while j < len(s):
            x = s[j]
            if x in m1:
                m2[x] = m2.get(x, 0) + 1
                if m2[x] == m1[x]:
                    have += 1
                while have == need and i <= j:
                    toDel = s[i]
                    if toDel in m2:
                        if m2[toDel] == m1[toDel]:
                            have -= 1
                        if res > j - i:
                            i_res, j_res, res = i, j, j - i
                        m2[toDel] -= 1

                    i += 1
            j += 1

        return "" if res == 1001 else s[i_res:j_res+1]

        