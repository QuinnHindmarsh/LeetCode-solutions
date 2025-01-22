class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        cnt = 0

        for word in words:
            cnt += 1
            for c in word:
                if c not in allowedSet:
                    cnt -= 1
                    break

        return cnt