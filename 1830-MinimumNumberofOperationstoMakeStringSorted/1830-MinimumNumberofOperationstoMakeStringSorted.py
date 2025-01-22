class Solution:
    def makeStringSorted(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # Fermat's Little Theorem for modular inverse
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
            
        # Count the frequency of each character
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
            
        result = 0
        for i, char in enumerate(s):
            # Count the number of characters smaller than the current character
            for j in range(ord(char) - ord('a')):
                if count[j] > 0:
                    count[j] -= 1
                    # Calculate the number of permutations with the remaining characters
                    total_permutations = fact[n - i - 1]
                    for c in count:
                        total_permutations = total_permutations * inv_fact[c] % MOD
                    result = (result + total_permutations) % MOD
                    count[j] += 1
            
            # Decrease the count of the current character
            count[ord(char) - ord('a')] -= 1
        
        return result
