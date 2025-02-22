class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(speed)
        time = [0] *n
        killed = 0

        for i in range(n):
            time[i] = dist[i] / speed[i]

        time.sort()

        for i in range(n):
            if time[i] <= killed:
                break
            killed += 1
        return killed