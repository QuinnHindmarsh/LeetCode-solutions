class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans = 0
        n = len(words)
        cnt = Counter(letters)

        for i in range(1 << n):
            cur_count = Counter(''.join(words[j] for j in range(n) if (i >> j) & 1))

            if all(cur_count[letter] <= cnt[letter] for letter in  cur_count):
                cur_score = sum(cur_count[letter] * score[ord(letter) - ord('a')] for letter in cur_count)
                ans = max(ans,cur_score)
        
        return ans
