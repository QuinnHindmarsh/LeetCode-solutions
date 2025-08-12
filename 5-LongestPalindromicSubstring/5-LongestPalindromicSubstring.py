# Last updated: 12/08/2025, 18:02:51
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        rem = 0

        for i in range(len(word)):
            rem *= 10
            rem += int(word[i])
            rem %= m

            ans.append(1 if rem == 0 else 0)
        return ans