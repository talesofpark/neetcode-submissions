class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #not sorted, shldnt sort
        #profit default 0 if not better than this
        #sliding window 
        #keep track of curr and best profit, and only change when curr > max 
        #two pointers?

        max_profit = 0 
        i,j = 0,1
        while j< len(prices):
            curr_profit = prices[j]-prices[i]
            if curr_profit > max_profit:
                max_profit = curr_profit 
                j+=1
            elif prices[j] < prices[i]:
                i=j
                j+=1
            else:
                j+=1

        return max_profit


            