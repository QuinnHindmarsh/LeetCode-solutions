class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) //3

        left = []
        right = []

        for i in range(n):
            left.append(-nums[i])
            right.append(nums[-i-1])

        heapq.heapify(left)
        heapq.heapify(right)

        leftSum = -sum(left)
        rightSum = sum(right)
        
        best = leftSum - rightSum 

        prefix = [leftSum]

        for i in range(n):
            current = nums[n+i]
            leftc = -left[0]

            if current < leftc:
                leftSum = leftSum - leftc + current
                heapq.heappush(left,-current)
                heapq.heappop(left)
            prefix.append(leftSum)

        suffix = [rightSum]

        for i in range(n):
            current = nums[n + n -i-1]
            rightc = right[0]
            if current > rightc:
                rightSum = rightSum - rightc + current
                heapq.heappush(right, current)
                heapq.heappop(right)
            suffix.append(rightSum)
        
        suffix.reverse()

        for x,y in zip(prefix,suffix):
            best = min(best,x-y)

        return best
