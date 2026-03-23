# Last updated: 23/03/2026, 20:13:14
1class Solution:
2    def sortSentence(self, s: str) -> str:
3        arr = s.split()
4        new = [''] * len(arr)
5
6        for word in arr: 
7            new[int(word[-1])-1] = word[0:len(word)-1]
8
9
10        return ' '.join(new)