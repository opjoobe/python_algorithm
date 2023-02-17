# Leetcode # 2558. Take Gifts From the Richest Pile

from heapq import heapify, heappush, heappop
class Solution(object):
    def pickGifts(self, gifts, k):
        gifts = list(map(lambda x: -x, gifts))
        heapify(gifts)
        for _ in range(k):
            now_max = - heappop(gifts)
            heappush(gifts, - int(now_max ** 0.5))
        return - sum(gifts)
