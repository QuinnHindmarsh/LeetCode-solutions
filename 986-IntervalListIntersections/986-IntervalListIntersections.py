# Last updated: 23/06/2025, 12:50:39
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        j = i = 0
        res = []

        while i != len(firstList) and j != len(secondList):
            if firstList[i][0] <= secondList[j][0]:
                a,b = firstList[i], secondList[j]
            else:
                a,b = secondList[j], firstList[i]

            if a[1] >= b[0]:
                res.append([b[0], min(a[1], b[1])])

            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return res
                