class MinStack:

    def __init__(self):
        self.stack = []
        self.monoStack = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.monoStack[-1]:
            self.monoStack.append(val)

    def pop(self) -> None:
        v = self.stack.pop()
        if v == self.monoStack[-1]:
            self.monoStack.pop()
        return v

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.monoStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()