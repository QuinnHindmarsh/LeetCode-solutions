# Last updated: 10/05/2026, 12:13:21
1class Solution:
2    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
3        freq = defaultdict(int)
4        ans = []
5        
6        
7        formed_chunk = re.split(r' |--',''.join(chunks))
8        for word in formed_chunk:
9            if not word:
10                continue
11            word = list(word)
12            if word[0] == '-': 
13                word.pop(0)
14            if not word:
15                continue
16            if word[-1] == '-': 
17                word.pop()
18
19            freq[''.join(word)] += 1
20
21
22        for query in queries: 
23            ans.append(freq[query])
24
25        return ans