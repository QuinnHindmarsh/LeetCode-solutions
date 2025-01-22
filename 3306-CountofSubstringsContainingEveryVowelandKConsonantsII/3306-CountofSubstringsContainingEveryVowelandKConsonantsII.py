class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vs = "aeiou"

        f = collections.Counter()
        cons = [-1]
        ccount = 0

        ans = 0
        lp = 0 

        for rp in range(n):
            c = word[rp]   
            
            if c in vs:
                f[c]+=1
            
            else:
                cons.append(rp)
                ccount +=1

            while ccount > k:
                c = word[lp]
                if c in vs:
                    f[c] -=1
                else:
                    ccount -=1
                lp +=1

            if ccount == k:
                while all(f[v] >= 1 for v in vs):
                    c = word[lp]
                    if c in vs:
                        f[c] -=1
                        lp += 1
                    else:
                        break
                if all(f[v] >= 1 for v in vs):
                    ans += lp - (cons[-(k+1)])
                else:
                    ans += lp - (cons[-(k+1)]+1)
                    
            
        return ans