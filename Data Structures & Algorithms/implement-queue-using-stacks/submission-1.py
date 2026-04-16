class MyQueue:

    def __init__(self):
        self.s1, self.s2 = [], []        

    def push(self, x: int) -> None:
        self.s1.append(x)
        
    def pop(self) -> int:
        while self.s1:
            x = self.s1.pop()
            self.s2.append(x)

        el = self.s2.pop()

        while self.s2:
            x = self.s2.pop()
            self.s1.append(x)
        return el

    def peek(self) -> int:
        while self.s1:
            x = self.s1.pop()
            self.s2.append(x)

        el = self.s2[-1]
        while self.s2:
            x = self.s2.pop()
            self.s1.append(x)
        return el

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()