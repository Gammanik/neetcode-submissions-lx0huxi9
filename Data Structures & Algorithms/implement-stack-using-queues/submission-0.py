import queue

class MyStack:

    def __init__(self):
        self.curr = queue.Queue()
        self.tmp = queue.Queue()
        

    def push(self, x: int) -> None:
        self.tmp.put(x)

        while not self.curr.empty():
            self.tmp.put(self.curr.get())

        self.curr, self.tmp = self.tmp, self.curr

    def pop(self) -> int:
        return self.curr.get()

    def top(self) -> int:
        return self.curr.queue[0]

    def empty(self) -> bool:
        return self.curr.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()