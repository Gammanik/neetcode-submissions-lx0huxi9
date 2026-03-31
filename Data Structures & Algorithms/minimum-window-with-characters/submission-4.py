from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        m1, m2 = Counter(t), {}
        need, have = sum(m1.values()), 0
        i, j = 0, 0
        i_res, j_res, res = 0, 0, 1001

        while j < len(s):
            x = s[j]
            if x in m1:
                m2[x] = m2.get(x, 0) + 1
                if m2[x] == m1[x]:
                    have += m1[x]
                    print(m1, m2, have, need)
                    while have >= need and i <= j:
                        print("~", i, j, have, m2)
                        toDel = s[i]
                        if toDel in m2:
                            if m2[toDel] == m1[toDel]:
                                have -= m1[toDel]
                            if res > j - i:
                                i_res, j_res, res = i, j, j - i
                            m2[toDel] -= 1

                        i += 1
            print(s[j], i, j, m2)
            j += 1

        # print("res", i_res, j_res, res)
        return "" if i_res == 0 and j_res == 0 and res == 1001 else s[i_res:j_res+1]

        