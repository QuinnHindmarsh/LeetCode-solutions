class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        cheapest_chocolate = second_cheapest_chocolate = float('inf')

        if len(prices) < 2:
            return money

        for chocolate_price in prices:
            if chocolate_price < cheapest_chocolate:
                second_cheapest_chocolate, cheapest_chocolate = cheapest_chocolate, chocolate_price
            elif chocolate_price < second_cheapest_chocolate:
                second_cheapest_chocolate = chocolate_price
        

        return money - (cheapest_chocolate + second_cheapest_chocolate) if cheapest_chocolate + second_cheapest_chocolate <= money else money