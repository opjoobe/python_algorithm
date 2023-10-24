# Leetcode # 1475. Final Prices With a Special Discount in a Shop

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices.copy()
        stack = []
        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                answer[stack.pop()] -= price
            stack.append(idx)
        return answer
        