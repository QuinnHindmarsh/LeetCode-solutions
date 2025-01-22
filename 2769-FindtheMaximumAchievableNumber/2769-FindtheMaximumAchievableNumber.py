class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        def find_max(num, t):
            if t == 0:
                return num
            return find_max(num+2, t-1)

        return find_max(num, t)