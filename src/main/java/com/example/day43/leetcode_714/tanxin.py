from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res = 0
        minPrice = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] > minPrice + fee:
                res += prices[i] - minPrice - fee
                minPrice = prices[i] - fee
            else:
                continue
        return res