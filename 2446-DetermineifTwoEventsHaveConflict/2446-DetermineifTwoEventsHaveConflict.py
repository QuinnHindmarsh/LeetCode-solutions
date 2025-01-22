class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0] <= event2[1] if event1[0] > event2[0] else event2[0] <= event1[1]