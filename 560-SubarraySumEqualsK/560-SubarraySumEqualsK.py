# Last updated: 23/06/2025, 15:08:01
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        map = defaultdict(int)
        map[0] += 1
        cnt = 0

        for num in nums:
            cur_sum += num

            cnt += map[cur_sum - k]
            map[cur_sum] += 1

        return cnt