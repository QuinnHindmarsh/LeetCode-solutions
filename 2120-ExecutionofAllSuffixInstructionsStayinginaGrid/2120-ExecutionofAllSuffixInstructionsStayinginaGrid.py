# Last updated: 17/08/2025, 11:41:04
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def valid(x,y):
            return 0 <= x < n and 0 <= y < n
        
        ans = []
        moves = {'U':[-1,0], 'D':[1,0], 'L':[0,-1],'R':[0,1]}

        for i in range(len(s)):
            mx = 0
            r,c = startPos

            for j in range(i,len(s)):
                move = moves[s[j]]
                r += move[0]
                c += move[1]

                if not valid(r,c):
                    break
                mx += 1
            
            ans.append(mx)

        return ans





        