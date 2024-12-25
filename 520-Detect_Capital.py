"""
520. Detect Capital
https://leetcode.com/problems/detect-capital/description/
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
"""

# Solution one, O(n) time and space - 3 O(n) itterations


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # All upper case
        if word.upper() == word:
            return True
        # All lower case
        if word.lower() == word:
            return True
        # Tittle case
        if word[0].upper() == word[0] and word[1::].lower() == word[1::]:
            return True

        # No conditions are true
        return False

# Solution two, O(n) time, O(1) space - 3 O(n) itterations


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Checks if the word is either uppercase, lowercase or tittle case
        return word.isupper() or word.islower() or word.istitle()

# Solution three, O(n) time and O(1) space - 1 O(n) itteration


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Condition is always true on words of length 1 or less
        if len(word) <= 1:
            return True

        # Uppercase first letter
        if ord(word[0]) <= 90:
            # Uppercase second letter - if any past this are lowercase no conditions are met
            if ord(word[1]) <= 90:
                for i in range(2, len(word), 1):
                    if ord(word[i]) > 90:
                        return False
            # Lowercase second letter - if any past this are uppercase no conditions are met
            else:
                for i in range(2, len(word), 1):
                    if ord(word[i]) <= 90:
                        return False
        # Lowercase first letter
        else:
            # If any letters past this are uppercase no conditions are met
            for i in range(1, len(word), 1):
                if ord(word[i]) <= 90:
                    return False

        # Exactly one criteria is met
        return True


# My solution
# https://leetcode.com/problems/detect-capital/solutions/6183339/simple-clear-solution-by-quinnhindmarsh-1c4f/
