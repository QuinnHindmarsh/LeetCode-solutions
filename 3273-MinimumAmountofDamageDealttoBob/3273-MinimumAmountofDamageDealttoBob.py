class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        arr = []
        ans = 0
        total = sum(damage)

        for i in range(n):
            health[i] = (health[i] + (power-1)) // power

        for i in range(n):
            d = damage[i]
            h = health[i]
            arr.append((d/h,-h,d))

        arr.sort()

        for i in range(n-1,-1,-1):
            ans += -arr[i][1] * total
            total -= arr[i][2]
        
        return ans