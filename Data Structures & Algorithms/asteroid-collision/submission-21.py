class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        res = []

        for a in asteroids:
            if a > 0:
                st.append(a)
            else:
                if not st:
                    res.append(a)
                    continue

                if abs(st[-1]) == abs(a):
                    st.pop()
                    continue

                if abs(st[-1]) > abs(a):
                    continue
                else:
                    st.pop()

                    flag = False
                    while st and st[-1] > 0 and abs(a) >= st[-1] and not flag:
                        if abs(a) == st[-1]:
                            flag = True
                            st.pop()
                            continue
                        st.pop()

                    if not st and not flag:
                        res.append(a)


        for s in st:
            res.append(s)

        return res
        