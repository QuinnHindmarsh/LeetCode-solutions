
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Find closest and get closest where taken from https://www.geeksforgeeks.org/find-closest-number-array/ 
        def findClosest(arr, n, target):
            i = 0
            j = n
            mid = 0
            while (i < j):
                mid = (i + j) // 2

                if (arr[mid] == target):
                    return arr[mid]

                if (target < arr[mid]):

                    if (mid > 0 and target > arr[mid - 1]):
                        return getClosest(arr[mid - 1], arr[mid], target)

                    j = mid
                else:
                    if (mid < n - 1 and target < arr[mid + 1]):
                        return getClosest(arr[mid], arr[mid + 1], target)
                    i = mid + 1

            return arr[mid]

        def getClosest(val1, val2, target):

            if (target - val1 >= val2 - target):
                return val2
            else:
                return val1


        maxDist = 0
        houses.sort()
        heaters.sort()

        n = len(houses)
        m = len(heaters)

        
        for i in range(n):
            maxDist = max(maxDist,abs(houses[i] - findClosest(heaters,m,houses[i])))
            
        return maxDist