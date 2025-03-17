class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_arr = []
        mx_candies = max(candies)
        for child in candies:
            if child + extraCandies >= mx_candies:
                bool_arr.append(True)
            else:
                bool_arr.append(False)

        return bool_arr 