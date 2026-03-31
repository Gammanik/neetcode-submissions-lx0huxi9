class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sc = {}
        n = len(s)
        mx = 1

        l, r = 0, 0
        while r < n:
            sc[s[r]] = sc.get(s[r], 0) + 1
            real_k = sum(sc.values()) - max(sc.values())

            mx = max(mx, r - l)
            while real_k > k and l < r:
                sc[s[l]] -= 1 if sc[s[l]] > 1 else sc.pop(s[l])
                real_k = sum(sc.values()) - max(sc.values())
                l += 1

            r += 1

        mx = max(mx, r - l)
        return mx

        # i = 0
        # while i < n:
        #     ch_cnt = {}
        #     for j in range(i,n):
        #         cycles += 1
        #         ch_cnt[s[j]] = ch_cnt.get(s[j],0) + 1

        #         mx_key = max(ch_cnt, key=ch_cnt.get)
        #         replace = sum(ch_cnt.values()) - ch_cnt[mx_key]

        #         if replace > k:
        #             ch_cnt = {}
        #             break
        #         else:
        #             mx = max(mx, sum(ch_cnt.values()))
        #     i += 1
        
        # return mx