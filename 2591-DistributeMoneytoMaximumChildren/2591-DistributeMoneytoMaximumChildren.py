class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # Not possible to distribute money
        if children > money:
            return -1
        # Gives each children $1
        money -= children 
        
        # The min of this is the max that could have 8
        ans = min(money // 7, children)
        money -= ans * 7
        
        # If there is still money and children left, one child will need
        # to be given more money, thus not have exactly 8
        if ans - children == 0 and money != 0:
            return ans - 1
        # If there is exactly one child and exactly 3 left, that money will 
        # need to be split across 2 children as no child can have $4
        if children - ans == 1 and money == 3:
            return ans -1
        return ans  