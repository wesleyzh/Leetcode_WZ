class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == []: return 0
        
        lowest, profit = prices[0], 0
        
        for i in range(len(prices)):
            profit = max(profit, prices[i] - lowest)
            lowest = min(lowest, prices[i])
            
        
        return profit
    
    

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            profit += prices[i] - prices[i-1] if prices[i] - prices[i-1] > 0 else 0
        
        return profit
    
    
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0: return 0
        
        #dynmaic programming, find the maximum profit before i and after i
        f1 = [0 for i in range(len(prices))]
        f2 = [0 for i in range(len(prices))]
        
        lowest = prices[0]
        for i in range (1, len(prices)):
            lowest = min(lowest, prices[i])
            f1[i] = max(f1[i-1], prices[i]-lowest)
        
        highest = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            highest = max(highest, prices[i])
            f2[i] = max(f2[i+1], highest - prices[i])
            
            
        res = 0
        for i in range(len(prices)):
            if f1[i] + f2[i] > res: res = f1[i] + f2[i]
        return res

        