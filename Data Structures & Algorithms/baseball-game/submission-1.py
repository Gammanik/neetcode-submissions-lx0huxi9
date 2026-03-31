class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []


        for o in operations:
            if o == "C":
                s.pop()
            elif o == 'D':
                s.append(s[-1] * 2)
            elif o == '+':
                res = s[-1] + s[-2]
                s.append(int(res))
            else:
                s.append(int(o))

        return sum(s)

