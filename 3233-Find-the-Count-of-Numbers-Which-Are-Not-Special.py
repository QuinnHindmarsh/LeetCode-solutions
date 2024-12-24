"""
https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/description/

You are given 2 positive integers l and r. For any number x, all positive divisors of x except x are called the proper divisors of x.

A number is called special if it has exactly 2 proper divisors. For example:

The number 4 is special because it has proper divisors 1 and 2.
The number 6 is not special because it has proper divisors 1, 2, and 3.
Return the count of numbers in the range [l, r] that are not special.
"""


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


"""
Complexity
Time complexity:
O(√r(lg(lg(√r))))

The Sieve of Eratosthenes takes O(n(lg(lg(n)))) time to generate all primes up to n. In this situation we generate all numbers up to √r. So this becomes O(√r(lg(lg(√r)))))

We then itterate over all of these prime numbers, doing a constant amount of work for each. There are at most √r prime numbers between 1 and √r. So this would be O(√rlg(lg(√r))+√r) which simplifies to O(√r(lg(lg(√r)))).

To be more accurate we can say there are approximitly ln(√r) primes, where ln ln(√r) is the natural log of the square root of r.

Space complexity:

O(√r)

Sieve of Eratosthenes takes O(n) space to generate all primes up to n. In this case we are generating all primes up to √r so it becomes O(√r).

"""

# My solution link
# https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/solutions/6179390/prime-number-sieve-of-eratosthenes-solut-qeny/
