class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        x = prices[0]
        i = 0
        y = 0
        max_profit = 0
        while i < len(prices):
            if len(prices) == 1:
                return 0
            elif x > prices[i]:
                x = prices[i]
                y = prices[i] - x
                if y > max_profit:
                    max_profit = y
            elif x < prices[i]:
                y = prices[i] - x
                if y > max_profit:
                    max_profit = y
            i += 1
        return max_profit
    
solu = Solution()
print(solu.maxProfit([7,6,4,3,1]))
            
