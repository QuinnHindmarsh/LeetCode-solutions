class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_frequency = defaultdict(int)
        max_lucky_num = -1

        for num in arr:
            num_frequency[num] += 1

        for num_key in num_frequency:
            if num_key == num_frequency[num_key]:
                max_lucky_num = max(max_lucky_num, num_key)

        return max_lucky_num