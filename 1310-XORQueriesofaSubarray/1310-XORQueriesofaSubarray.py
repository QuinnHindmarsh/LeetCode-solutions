from math import inf
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        results = []
        prefixes = [0]

        for n in arr:
            prefixes.append(prefixes[-1] ^ n)
        
        for left,right in queries:
            results.append(prefixes[right+1]^prefixes[left])
        
        return results