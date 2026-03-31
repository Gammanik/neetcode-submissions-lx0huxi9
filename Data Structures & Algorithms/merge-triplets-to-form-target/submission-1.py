class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        ar, br, cr = 0, 0, 0

        for a_, b_, c_ in triplets:
            if a_ <= a and b_ <= b and c_ <= c:
                if a_ == a or b_ == b or c_ == c:
                    ar = max(ar, a_)
                    br = max(br, b_)
                    cr = max(cr, c_)

        print(ar, br, cr)
        return a == ar and b == br and c == cr
        