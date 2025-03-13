class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitSum = 0
        elementSum = 0

        for num in nums:
            elementSum += num
            while num > 0:
                digit = num % 10
                num = num // 10
                digitSum += digit
        if digitSum > elementSum:
            return digitSum - elementSum
        else: return elementSum - digitSum
