# Last updated: 23/03/2026, 20:36:01
1class Solution:
2    def maximumEvenSplit(self, finalSum: int) -> List[int]:
3        cur_sum = 0
4        last_num = 0
5        nums = []
6
7        if finalSum % 2 == 1:
8            return []
9
10        while cur_sum < finalSum:
11            last_num += 2
12            if cur_sum + last_num > finalSum:
13                nums[-1] += finalSum - cur_sum
14                break
15            else:
16                cur_sum += last_num
17                nums.append(last_num)
18
19        return nums