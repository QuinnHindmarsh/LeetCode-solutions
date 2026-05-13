# Last updated: 13/05/2026, 21:10:48
1class MagicDictionary:
2    def __init__(self):
3        self.mp = defaultdict(list)
4
5    def buildDict(self, dictionary: List[str]) -> None:
6        for w in dictionary:
7            self.mp[len(w)].append(w)
8
9    def search(self, searchWord: str) -> bool:
10        for w in self.mp[len(searchWord)]:
11            if sum(a != b for a, b in zip(w, searchWord)) == 1:
12                return True
13        return False