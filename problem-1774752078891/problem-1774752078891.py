# Last updated: 29/03/2026, 13:11:18
1class EventManager:
2
3    def __init__(self, events: list[list[int]]):
4        self.tree = SortedList()
5        self.map = {}
6
7        for id,priority in events: 
8            self.map[id] = priority
9            self.tree.add((priority,-id))
10
11    def updatePriority(self, eventId: int, newPriority: int) -> None:
12        if eventId in self.map: 
13            self.tree.remove((self.map[eventId],-eventId))
14
15        self.map[eventId] = newPriority
16        self.tree.add((newPriority,-eventId))
17
18    def pollHighest(self) -> int:
19        if not self.tree: 
20            return -1
21        return -self.tree.pop()[1]
22
23        
24        
25
26
27# Your EventManager object will be instantiated and called as such:
28# obj = EventManager(events)
29# obj.updatePriority(eventId,newPriority)
30# param_2 = obj.pollHighest()