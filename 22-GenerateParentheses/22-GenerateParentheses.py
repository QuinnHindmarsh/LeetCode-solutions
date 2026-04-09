# Last updated: 09/04/2026, 12:34:54
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        valid = []
4
5        def backtrack(ro,rc,state):
6
7            if ro == rc == 0: 
8                valid.append(''.join(state))
9                return 
10
11            if rc > ro: 
12                state.append(')')
13                backtrack(ro,rc-1,state)
14                state.pop()
15            if ro != 0: 
16                state.append('(')
17                backtrack(ro-1,rc,state)
18                state.pop()
19
20        backtrack(n,n,[])
21        return valid