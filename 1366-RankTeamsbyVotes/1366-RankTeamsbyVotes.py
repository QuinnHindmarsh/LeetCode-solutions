# Last updated: 09/04/2025, 21:42:27
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        votes_map = {}
        team_cnt = len(votes[0])
        formated_votes_arr = []

        for vote in votes:
            for team_idx in range(len(vote)):
                team_letter = vote[team_idx]

                if team_letter not in votes_map:
                    votes_map[team_letter] = [0] * team_cnt

                votes_map[team_letter][team_idx] -= 1

        votes_arr = sorted(votes_map, key = lambda team_letter:(votes_map[team_letter], team_letter) )


        for team in votes_arr:
            formated_votes_arr.append(team[0])

        return ''.join(formated_votes_arr)
        
        
