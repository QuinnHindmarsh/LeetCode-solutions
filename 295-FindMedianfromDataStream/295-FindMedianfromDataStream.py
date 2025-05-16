# Last updated: 16/05/2025, 18:39:36
class MedianFinder:

    def __init__(self):
        #python defult is min, for max *-1
        self.left = [] # max heap
        self.right = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.left or -self.left[0] >= num:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        self.rebalance()


    def findMedian(self) -> float:
        if len(self.right) == len(self.left):
            return (self.right[0] + (self.left[0] *-1)) /2
        else:
            return self.left[0] *-1

    def rebalance(self):
        while len(self.left) > len(self.right) +1:
            top = heapq.heappop(self.left)
            heapq.heappush(self.right, top *-1)

        while len(self.left) < len(self.right):
            top = heapq.heappop(self.right)
            heapq.heappush(self.left, top *-1)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()