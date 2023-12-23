# Leetcode # 2706. Buy Two Chocolates

from heapq import heapify, heappop
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapify(prices)
        first = heappop(prices)
        second = heappop(prices)
        leftover = money - first - second
        return leftover if leftover >= 0 else money
