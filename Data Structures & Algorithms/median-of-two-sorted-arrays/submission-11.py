class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b): a, b = b, a

        m, n = len(a), len(b)
        l, r = 0, m
        total = m + n
        half = total // 2

        while True:
            i = (l + r) // 2
            j = half - i
            
            al = a[i-1] if i > 0 else float('-inf')
            ar = a[i] if i < m else float('inf')
            bl = b[j-1] if j > 0 else float('-inf')
            br = b[j] if j < n else float('inf')

            if al <= br and ar >= bl:
                if total % 2 == 0:
                    return (max(al, bl) + min(ar, br)) / 2
                else:
                    return min(ar, br)

            if al > br:
                r = i-1
            else:
                l = i+1
                

        