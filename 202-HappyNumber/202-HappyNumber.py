class Solution:
    def isHappy(self, n: int) -> bool:
        def squareVal(num):
            num = str(num)
            ans = 0
            for i in range(len(num)):
                ans += int(num[i]) ** 2
            return ans
        
        slow = squareVal(n)
        fast = squareVal(squareVal(n))

        while True:
            if fast == 1 or slow == 1:
                return True
            if fast == slow:
                return False
            
            slow = squareVal(slow)
            fast = squareVal(squareVal(fast))