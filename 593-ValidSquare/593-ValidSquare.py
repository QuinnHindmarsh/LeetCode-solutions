# Last updated: 04/04/2026, 12:34:27
1class Solution:
2
3    def validSquare(self, p1, p2, p3, p4):
4        def dist2(a, b):
5            return (a[0]-b[0])**2 + (a[1]-b[1])**2
6
7        points = [p1, p2, p3, p4]
8        dists = sorted(dist2(points[i], points[j])
9                    for i in range(4) for j in range(i+1, 4))
10
11        # 4 equal sides, 2 equal diagonals, no zero-length sides
12        return dists[0] > 0 and dists[0] == dists[3] and dists[4] == dists[5]