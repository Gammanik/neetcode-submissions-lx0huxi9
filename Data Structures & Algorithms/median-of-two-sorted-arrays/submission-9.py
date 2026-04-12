class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b): a, b = b, a

        l, r = 0, len(a) - 1
        total = len(a) + len(b)
        half = total // 2 - 1

        if len(a) == 0:
            if len(b) % 2 == 0:
                return (b[half] + b[half+1]) / 2
            else:
                return b[half+1]

        while True:
            m = (l + r) // 2
            print(l, r, m)

            if m == -1:
                if total % 2 == 0:
                    return b[half] + min(a[0], b[half+1]) / 2
                else:
                    return min(a[0], b[half + 1])
            
            a1, a2 = a[m], 9999999 if m >= len(a)-1 else a[m+1]
            b1, b2 = b[half-m-1], 9999999 if half-m >= len(b) else b[half-m]
            print('~', a1, a2, b1, b2)

            if half-m-1 < 0:
                b1 = -1

            if a1 <= b2 and a2 >= b1:
                if total % 2 == 0:
                    l, r = max(a1, b1), min(a2, b2)
                    return (l + r) / 2
                else:
                    return max(a2, b1)

            if a1 > b2:
                r = m-1
            else:
                l = m+1
                

        