class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        n = len(boxes)

        for i in range(n):
            cur = 0
            for j in range(n):
                if boxes[j] == '1':
                    cur += abs(i-j)
            ans.append(cur)
        return ans