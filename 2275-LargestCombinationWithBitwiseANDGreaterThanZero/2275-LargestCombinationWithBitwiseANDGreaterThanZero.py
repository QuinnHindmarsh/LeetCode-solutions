class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        places = {}

        for num in candidates:
            binRep = bin(num)[2:]
            binRep = binRep[::-1]
            for i in range(len(binRep)):
                if binRep[i] == '1':
                    if i in places:
                        places[i] += 1
                    else:
                        places[i] =1 

        Max = 0
        for key in places:
            if places[key] > Max:
                Max = places[key]

        return Max