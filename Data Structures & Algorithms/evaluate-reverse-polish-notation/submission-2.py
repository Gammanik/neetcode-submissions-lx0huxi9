class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.s = []

        for t in tokens:
            print(self.s)
            if t in ('+', '-', '*', '/'):
                b = self.s.pop()
                a = self.s.pop()

                if t == '+':
                    self.s.append(int(a) + int(b))
                if t == '-':
                    self.s.append(int(a) - int(b))
                if t == '*':
                    self.s.append(int(a) * int(b))
                if t == '/':
                    self.s.append(int(a) / int(b))
            else:
                self.s.append(t)

        return int(self.s[-1])