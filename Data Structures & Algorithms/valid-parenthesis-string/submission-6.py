class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        st2 = []

        for i, c in enumerate(s):
            if c == ')':
                if not st:
                    if not st2:
                        return False
                    else:
                        st2.pop()
                else:
                    st.pop()
            if c == '(':
                st.append(i)

            if c == '*':
                st2.append(i)

        if len(st) > len(st2):
            return False

        print(st, st2)

        j = 0
        for i in range(len(st)):
            while j < len(st2) and st[i] > st2[j]:
                j += 1

            if j >= len(st2):
                return False
            j += 1
        
        return True