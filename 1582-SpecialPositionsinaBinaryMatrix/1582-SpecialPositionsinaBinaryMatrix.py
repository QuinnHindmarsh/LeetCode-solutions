class Solution:
    def numSpecial(self, arr: List[List[int]]) -> int:
        rows = [{} for _ in range(len(arr))]
        cols = [{} for _ in range(len(arr[0]))]
        cnt = 0

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                val = arr[i][j]
                rows[i][val] = rows[i].get(val, 0) +1
                cols[j][val] = cols[j].get(val, 0) +1

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 1:
                    # if 0 in rows[i] and cols[i]
                    if rows[i][1] == 1 and cols[j][1] == 1:
                        cnt += 1
        return cnt