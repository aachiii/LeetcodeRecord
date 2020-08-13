'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most !!!two!!! transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # forward traversal, profits record the max profit 
        # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)
        print(profits)

        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction 
        total_max = 0    
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])
            print(max_profit)

        return total_max
      
'''

First traversal gets maximum profit until x day.
Second backward traversal gets maximum profit since x day.

'''

