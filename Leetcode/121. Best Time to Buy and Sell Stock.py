# Leetcode # 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        now_max = 0
        for price in reversed(prices):
            if now_max < price:
                now_max = price
            else:
                answer = max(answer, now_max - price)
        return answer