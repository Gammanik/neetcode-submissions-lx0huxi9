class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(mx_cap) -> bool:        
            curr_s = 0
            days_curr = 0
            # print(mx_cap)
            for w in weights:
                if w > mx_cap:
                    return False
                
                # print(":", w, days_curr)
                if curr_s + w > mx_cap:
                    days_curr += 1
                    curr_s = w
                    continue

                if curr_s + w <= mx_cap:
                    curr_s += w

            # print(mx_cap, days_curr, days_curr <= days)
            return days_curr + 1 <= days

        l, r = min(weights), sum(weights)
        while l <= r:
            m = l + (r - l) // 2
            # print(l,r)
            if check(m):
                r = m-1
            else:
                l = m+1

        return l
        