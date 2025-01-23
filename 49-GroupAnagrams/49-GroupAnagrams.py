class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        groupArr = []   
        for word in strs:
            freqs = [0] * 26
            for c in word:
                freqs[(ord(c)-97)] += 1
            groups[tuple(freqs)].append(word)

        for key in groups:
            groupArr.append(groups[key])

        return groupArr