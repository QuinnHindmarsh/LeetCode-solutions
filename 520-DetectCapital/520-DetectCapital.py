class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        
        if ord(word[0]) <= 90:
            if ord(word[1]) <= 90:
                for i in range(2,len(word),1):
                    if ord(word[i]) > 90:
                        return False
            else:
                for i in range(2,len(word),1):
                    if ord(word[i]) <= 90:
                        return False
        else:
            for i in range(1,len(word),1):
                if ord(word[i]) <= 90:
                    return False

        return True