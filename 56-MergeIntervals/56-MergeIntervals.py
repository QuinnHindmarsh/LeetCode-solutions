# Last updated: 23/06/2025, 12:07:31
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort  = sorted(intervals, key = lambda x: (x[0], -x[1]))
        merged = []
        merged.append(sort[0])

        for i in range(1, len(sort)):
            if sort[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], sort[i][1])
            else:
                merged.append(sort[i])

        return merged