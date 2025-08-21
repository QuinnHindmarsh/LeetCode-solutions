# Last updated: 21/08/2025, 14:54:58
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr.sort(key= lambda y: (abs(y-x),y))

        return sorted(arr[0:k])