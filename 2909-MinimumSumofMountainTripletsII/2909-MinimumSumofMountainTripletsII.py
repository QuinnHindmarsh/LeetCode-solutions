# Last updated: 13/05/2026, 21:28:55
1class Solution:
2    def minimumSum(self, nums: List[int]) -> int:
3        n = len(nums)
4        prefix_min = [0] * n
5        suffix_min = [0] * n
6
7        prefix_min[0] = nums[0]
8        for i in range(1, n):
9            prefix_min[i] = min(prefix_min[i - 1], nums[i])
10
11        suffix_min[-1] = nums[-1]
12        for i in range(n - 2, -1, -1):
13            suffix_min[i] = min(suffix_min[i + 1], nums[i])
14
15        ans = float('inf')
16        for j in range(1, n - 1):
17            left = prefix_min[j - 1]
18            right = suffix_min[j + 1]
19            if left < nums[j] and right < nums[j]:
20                ans = min(ans, left + nums[j] + right)
21
22        return ans if ans != float('inf') else -1