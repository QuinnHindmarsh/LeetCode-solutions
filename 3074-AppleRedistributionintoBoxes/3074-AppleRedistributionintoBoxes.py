class Solution:
    def minimumBoxes(self, apples: List[int], capcaity: List[int]) -> int:
        
        ans = 0
        totalApples = sum(apples)
        capcaity.sort(reverse=True)
        for c in capcaity:
            ans += 1 
            totalApples -= c
            if totalApples <= 0:
                break
        return ans 