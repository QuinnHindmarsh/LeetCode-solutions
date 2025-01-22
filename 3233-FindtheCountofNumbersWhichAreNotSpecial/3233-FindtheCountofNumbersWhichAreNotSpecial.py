
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        # A number will be a special number if the square root of it is a prime.
        # The opposite is also true, a number will not be a special number if the square root of it is not prime

        # Sieve of Eratosthenes - generates all prime numbers up to n, in O(n log (log n))
        def Eratosthenes(num):
            if num <= 2:
                return []

            is_prime = [True] * num
            is_prime[0] = False
            is_prime[1] = False

            for i in range(2, num):
                if is_prime[i]:
                    for x in range(i*i, num, i):
                        is_prime[x] = False
            return [i for i in range(num) if is_prime[i]]

        # We need to generate prime numbers up to the square root of r, as we will be seeing
        # if a number is the square of a prime number
        primes = Eratosthenes(isqrt(r)+1)

        # Counts number of special numbers between  l and r
        special_count = 0
        # Itterates through all prime numbers, if the number squared is between l and r
        # That implies the square of it is a special number within that range
        for prime in primes:
            square = prime * prime
            if l <= square <= r:
                special_count += 1

        #   returns the total numbers between l and r, minus the amount of special numbers
        return (r-l + 1) - special_count