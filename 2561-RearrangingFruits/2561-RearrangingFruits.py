class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        b1 = {}
        b2 = {}
        b1Changes = []
        b2Changes = []
        ans = 0

        #make dictionaires for each basket 
        for val in (basket1):
            if val in b1:
                b1[val] +=1
            else:
                b1[val] = 1
        
        for val in (basket2):
            if val in b2:
                b2[val] +=1
            else:
                b2[val] = 1



        # Finds all items where b1 has more of them then b2, and adds the amount to move to a changes dir
        for key in b1:
            if key not in b2:
                n = b1[key]
                if n % 2 != 0:
                    return -1
                for i in range(n//2):
                    b2Changes.append(key)
            elif b1[key] > b2[key]:
                n = b1[key] + b2[key]
                if n % 2 != 0:
                    return -1
                for i in range((b1[key] - b2[key])//2):
                    b2Changes.append(key)


        # Opposite
        for key in b2:
            if key not in b1:
                n = b2[key]
                if n % 2 != 0:
                    return -1
                for i in range(n//2):
                    b1Changes.append(key)
            elif b2[key] > b1[key]:
                n = b1[key] + b2[key]
                if n % 2 != 0:
                    return -1
                for i in range((b2[key] - b1[key])//2):
                    b1Changes.append(key)
        

        if len(b1Changes) == 0:
            return 0

        # having one sorted ascending and one desncding will always maximise the difference between min and max, which is optimal 
        b1Changes.sort()
        b2Changes.sort(reverse=True)
        min_v = min(basket1 + basket2)

        for v1,v2 in zip(b2Changes,b1Changes):
            ans += min(v1,v2,min_v*2)
        return ans
