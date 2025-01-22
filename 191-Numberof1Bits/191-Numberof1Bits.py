class Solution:
    def hammingWeight(self, n: int) -> int:
        # Converts to binary and removes the first 2 chars '0b'
        c = bin(n)[2:]
        ans = 0

        for i in range(len(c)):
            # Adds the value of the binary to the current count
            ans += int(c[i])

        return ans