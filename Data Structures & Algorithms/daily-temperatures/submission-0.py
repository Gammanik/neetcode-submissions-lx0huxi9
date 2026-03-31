class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = []
        last_max, idx_max = 0, 0

        for idx, t in enumerate(list(reversed(temperatures))):
            if s:
                last_max, idx_max = s[-1]
            else:
                last_max, idx_max = 0, 0
            print(t, last_max, s)
            
            while s and t >= last_max:
                del s[-1]
                last_max, idx_max = s[-1] if s else (0, idx)
                print('del', t, last_max, t >= last_max)
            
            val = idx - idx_max

            res.append(val)
            s.append((t, idx))
            # print(res, s)


        print(s, res)
        return list(reversed(res))

        