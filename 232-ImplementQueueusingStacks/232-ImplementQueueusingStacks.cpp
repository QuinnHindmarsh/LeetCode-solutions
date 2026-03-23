// Last updated: 23/03/2026, 20:23:36
1class MyQueue {
2    stack<int> new_stack;
3    stack<int> old_stack;
4
5    void transfer() {
6        while (!new_stack.empty()) {
7            old_stack.push(new_stack.top());
8            new_stack.pop();
9        }
10    }
11
12public:
13    void push(int x) {
14        new_stack.push(x);
15    }
16
17    int pop() {
18        if (old_stack.empty()) transfer();
19        int val = old_stack.top();
20        old_stack.pop();
21        return val;
22    }
23
24    int peek() {
25        if (old_stack.empty()) transfer();
26        return old_stack.top();
27    }
28
29    bool empty() {
30        return new_stack.empty() && old_stack.empty();
31    }
32};