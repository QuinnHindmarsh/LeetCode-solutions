
class Solution(object):
    def sortByBits(self, arr):\
        # Converts each number to binary, counts the amount of 1's uses that as the main key, then when there are ties compares the Key itself
        return sorted(arr,key=lambda n:(bin(n)[2::].count('1'),n))




