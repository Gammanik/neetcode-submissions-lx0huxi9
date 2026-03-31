class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_cnt = {}
        n = len(s)
        mx = 1

        i = 0
        while i < n:
            ch_cnt = {}
            for j in range(i,n):
                ch_cnt[s[j]] = ch_cnt.get(s[j],0) + 1

                mx_key = max(ch_cnt, key=ch_cnt.get)
                replace = sum(ch_cnt.values()) - ch_cnt[mx_key]

                print(s[j], (i, j), mx_key, ch_cnt, replace)

                if replace > k:
                    ch_cnt = {}
                    break
                else:
                    mx = max(mx, sum(ch_cnt.values()))
            i += 1
        


        return mx