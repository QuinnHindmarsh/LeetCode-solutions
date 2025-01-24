class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)

        for i in range(n):
            numSet = set()
            numSet.add(nums[i])
            inbalance = 0
            for j in range(i+1,n):
                num = nums[j]
                if num -1 in numSet and num not in numSet:
                    inbalance -=1

                if num + 1 not in numSet and num not in numSet:
                    inbalance +=1 

                numSet.add(num)
                cnt += inbalance

        return cnt