class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # ans = 0

        # i = 0
        # while tickets[kp] != 0:
        #     if i == len(tickets):
        #         i = 0

        #     if tickets[i] != 0:
        #         tickets[i]-=1
        #         ans +=1
        #     i +=1

        # return ans

        ans = 0

        i = 0
        while i < len(tickets):
            if i <= k:
                ans += min(tickets[i],tickets[k])
            else:
                ans += min(tickets[i],tickets[k] -1)
            i +=1

        return ans

