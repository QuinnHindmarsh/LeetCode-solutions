class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        def isprime(num):
            for i in range(2,int(sqrt(num)) +1):
                if num % i == 0:
                    return False
            return True
        plim = math.log(num,2) + 1

        for i in range(int(plim)):
            if num == (2**(i-1)) * ((2**i) - 1) and isprime(2**i -1):
                return True
        return False
