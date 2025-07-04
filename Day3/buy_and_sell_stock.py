class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices);
        buy=float('inf');
        profit=0;
        for price in prices:
            if buy > price:
                buy = price;
            if (price - buy) > profit:
                profit = price-buy;
        
        return profit;
        