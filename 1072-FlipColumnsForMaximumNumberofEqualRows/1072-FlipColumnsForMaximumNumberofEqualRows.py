class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freqs = defaultdict(int)

        def flip(row):
            flipped = []
            for i in range(len(row)):
                flipped.append(abs(1- row[i]))

            return flipped

        for row in matrix:
            freqs[tuple(row)] += 1
            freqs[tuple(flip(row))] +=1

        mx = 0
        for key in freqs:
            mx = max(mx, freqs[key])

        return mx