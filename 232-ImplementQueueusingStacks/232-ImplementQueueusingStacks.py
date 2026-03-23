# Last updated: 23/03/2026, 20:21:21
1class MyQueue:
2
3    def __init__(self):
4        self.new_stack = []
5        self.old_stack = []
6
7        
8
9    def push(self, x: int) -> None:
10        self.new_stack.append(x)
11
12    def pop(self) -> int:
13        if self.old_stack:
14            return self.old_stack.pop()
15        else:
16            while self.new_stack:
17                self.old_stack.append(self.new_stack.pop())
18            return self.old_stack.pop()
19    def peek(self) -> int:
20        if self.old_stack:
21            return self.old_stack[-1]
22        else:
23            while self.new_stack:
24                self.old_stack.append(self.new_stack.pop())
25            return self.old_stack[-1]
26            
27
28    def empty(self) -> bool:
29        return not(self.old_stack or self.new_stack)
30
31
32# Your MyQueue object will be instantiated and called as such:
33# obj = MyQueue()
34# obj.push(x)
35# param_2 = obj.pop()
36# param_3 = obj.peek()
37# param_4 = obj.empty()