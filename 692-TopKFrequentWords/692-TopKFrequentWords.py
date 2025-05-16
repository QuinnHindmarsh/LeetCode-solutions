# Last updated: 16/05/2025, 18:01:27
class Pair:
    def __init__(self,str,freq):
        self.str = str
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.str < other.str

        return self.freq > other.freq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = Counter(words)
        heap = [Pair(str,freq) for str, freq in freqs.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap).str for _ in range(k)]
