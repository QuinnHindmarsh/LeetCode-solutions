class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Makes all stones neggitive to turn the min heap into a max heap
        for i in range(len(stones)):
            stones[i] *= -1

        heapify(stones)

        while stones:
            stone1 = heappop(stones)
            if stones:
                stone2 = heappop(stones)
            else:
                # Exactly one stone left, return the value of remaming stone
                return stone1 * -1

            # Makes sure no stones with weight of 0 are added
            # stone1 >= stone2. So the only condition we need to check is if they equal
            if stone1 != stone2:
                heappush(stones, stone1-stone2)
        # No stones left
        return 0

# My solution
# https://leetcode.com/problems/last-stone-weight/solutions/6179801/simple-heap-solution-by-quinnhindmarsh-x4gd/


"""
Complexity
Time complexity:
O(nlogn)

itterate over the heap turning each value negative O(n)
heapify the array O(n)
itterate over the heap - removing top 2 each time and adding the difference back in. this is still O(nlogn) even though stones can be added back, as they can only be added back a linear number of times
Space complexity:
O(n)
Due to the space taken up by the heap
"""
