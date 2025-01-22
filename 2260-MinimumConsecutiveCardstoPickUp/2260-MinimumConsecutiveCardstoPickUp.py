class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen =  {}
        ans = -1

        for i,c in enumerate(cards):
            if c in seen:
                ans = min(ans,i-seen[c]+1) if ans != -1 else i-seen[c] +1
                seen[c] = i
            else:
                seen[c] = i
        
        return ans 