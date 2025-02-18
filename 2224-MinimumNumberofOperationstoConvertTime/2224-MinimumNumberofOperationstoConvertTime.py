class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        diff = 0
        ans = 0

        diff += int(correct[0:2]) - int(current[0:2])
        diff *= 60

        diff += int(correct[3:5]) - int(current[3:5])

        ans += diff // 60
        diff %= 60

        ans += diff // 15
        diff %= 15

        ans += diff // 5
        diff %= 5

        ans += diff

        return ans