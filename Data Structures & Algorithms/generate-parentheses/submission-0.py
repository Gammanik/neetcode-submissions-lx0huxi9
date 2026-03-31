from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o = ['(' for _ in range(n)]
        c = [')' for _ in range(n)]
        s = ['(']  # первая открывающая уже использована
        self.res = []

        self.f(o[1:], c, s, ['('])
        return self.res

    def f(self, o: List[str], c: List[str], s: List[str], r: List[str]):
        if not o and not c:
            self.res.append(''.join(r))
            return

        # Добавить закрывающую скобку, если есть открытые в стеке и остались закрывающие
        if s and c:
            self.f(o, c[1:], s[:-1], r + [')'])

        # Добавить открытую скобку, если она осталась
        if o:
            self.f(o[1:], c, s + ['('], r + ['('])
